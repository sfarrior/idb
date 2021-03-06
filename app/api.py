import flask_restless
from models import Satellite, Planet, Star, Galaxy, Image

url_prefix = "/api/v1"

def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

def api_setup(flask_app, db) :
    manager = flask_restless.APIManager(flask_app, flask_sqlalchemy_db=db)
    flask_app.register_blueprint(api_setup_satellite(manager))
    flask_app.register_blueprint(api_setup_planet(manager))
    flask_app.register_blueprint(api_setup_star(manager))
    flask_app.register_blueprint(api_setup_galaxy(manager))
    
def api_setup_satellite(manager) :
    blueprint = {
        "model":Satellite,
        "methods":["GET"],
        "url_prefix":url_prefix,
        "collection_name":"satellites",
        "exclude_columns":["planet", "star", "galaxy", "image", "image_pid",
            "year_launched_str"],
        "include_methods":["model_type"],
        "results_per_page":9,
        "max_results_per_page":50
    }
    
    blueprint = manager.create_api_blueprint(**blueprint) 
    blueprint.after_request(add_cors_headers)    
    return blueprint

def api_setup_planet(manager) :
    blueprint = {
        "model":Planet,
        "methods":["GET"],
        "url_prefix":url_prefix,
        "collection_name":"planets",
        "exclude_columns":["satellites", "star", "galaxy", "image", "image_pid",
            "diameter_str", "ra_str", "dec_str", "gravity_str", "orbital_period_str",
            "mass_str", "temperature_str"],
        "include_methods":["model_type"],
        "results_per_page":9,
        "max_results_per_page":50
    }
    
    blueprint = manager.create_api_blueprint(**blueprint) 
    blueprint.after_request(add_cors_headers)    
    return blueprint

def api_setup_star(manager) :
    blueprint = {
        "model":Star,
        "methods":["GET"],
        "url_prefix":url_prefix,
        "collection_name":"stars",
        "exclude_columns":["satellites", "planets", "galaxy", "image", "image_pid",
            "diameter_str", "ra_str", "dec_str", "mass_str", "temperature_str"],
        "include_methods":["model_type"],
        "results_per_page":9,
        "max_results_per_page":50
    }
    
    blueprint = manager.create_api_blueprint(**blueprint) 
    blueprint.after_request(add_cors_headers)    
    return blueprint
    
def api_setup_galaxy(manager) :
    blueprint = {
        "model":Galaxy,
        "methods":["GET"],
        "url_prefix":url_prefix,
        "collection_name":"galaxies",
        "exclude_columns":["satellites", "planets", "stars", "image", "image_pid",
            "ra_str", "dec_str", "redshift_str", "size_str"],
        "include_methods":["model_type"],
        "results_per_page":9,
        "max_results_per_page":50
    }
    blueprint = manager.create_api_blueprint(**blueprint) 
    blueprint.after_request(add_cors_headers)    
    return blueprint

