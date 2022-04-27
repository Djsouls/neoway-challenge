from flask import jsonify

def format_response(controller_function):
    def wrapper(ref):
        result = controller_function(ref)

        return jsonify(result)

    return wrapper