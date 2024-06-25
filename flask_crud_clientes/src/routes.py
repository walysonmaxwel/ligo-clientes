import requests
from flask import render_template, request, jsonify
from . import app, db, logger
from .models import Client
import uuid
from datetime import datetime
from sqlalchemy.exc import IntegrityError

@app.route('/')
def index():
    clients = Client.query.all()
    for client in clients:
        client.inclusion_date = datetime.strptime(client.inclusion_date, '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')
    return render_template('index.html', clients=clients)

@app.route('/clients', methods=['POST'])
def add_client():
    data = request.get_json()

    client_id = str(uuid.uuid4())
    client_secret = str(uuid.uuid4())
    inclusion_date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    new_client = Client(
        name=data['name'],
        address=data['address'],
        email=data['email'],
        client_id=client_id,
        client_secret=client_secret,
        inclusion_date=inclusion_date
    )

    try:
        db.session.add(new_client)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        if 'client_address_key' in str(e.orig):
            return jsonify({'error': 'Endereço já existe'}), 400
        elif 'client_email_key' in str(e.orig):
            return jsonify({'error': 'Email já existe'}), 400
        else:
            return jsonify({'error': 'Constraint violation'}), 400
    except Exception as e:
        db.session.rollback()
        logger.error(f"Exception: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

    formatted_date = datetime.strptime(inclusion_date, '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')

    return jsonify({
        'id': new_client.id,
        'client_id': client_id,
        'client_secret': client_secret,
        'inclusion_date': formatted_date,
        'message': 'Cliente criado com sucesso!'
    })


@app.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    for client in clients:
        client.inclusion_date = datetime.strptime(client.inclusion_date, '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')
    return jsonify([client.to_dict() for client in clients])

@app.route('/generate_jwt/<int:client_id>', methods=['GET'])
def generate_jwt(client_id):
    client = Client.query.get(client_id)
    if not client:
        return jsonify({'error': 'Client not found'}), 404
    
    user_data = {
        "id": client.id,
        "name": client.name,
        "address": client.address,
        "email": client.email
    }

    expiration_time = 1 
    response = requests.post('http://fastapi_jwt:8000/generate_jwt', json=user_data, params={"expiration_time": expiration_time})
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to generate JWT'}), response.status_code
