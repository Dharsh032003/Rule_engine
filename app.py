import json

from flask import Flask, request, jsonify, send_from_directory
from rule_engine import create_rule, combine_rules, evaluate_rule, print_ast
from database import init_db, add_rule, get_all_rules, get_rule, delete_rule
import os

app = Flask(__name__)


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/api/rules', methods=['POST'])
def create_new_rule():
    data = request.json
    rule_string = data['rule']
    name = data['name']
    add_rule(name, rule_string)
    return jsonify(create_rule(rule_string).to_dict()), 201


@app.route('/api/rules', methods=['GET'])
def get_rules():
    rules = get_all_rules()
    return jsonify(rules)


@app.route('/api/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    rule_ids = data['rule_ids']
    user_data = json.loads(data['user_data'])

    try:
        rules = [get_rule(rule_id)[2] for rule_id in rule_ids]
        print(f"Rules to evaluate: {rules}")  # Debug print
        combined_rule = combine_rules(rules)
        if combined_rule is None:
            return jsonify({"error": "No valid rules to evaluate"}), 400

        print(f"Combined rule: {combined_rule}")  # Debug print
        result = evaluate_rule(combined_rule, user_data)
        print(f"Evaluation result: {result}")  # Debug print
        return jsonify({"result": result})
    except Exception as e:
        print(f"Error during evaluation: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/rules', methods=['DELETE'])
def delete_rules():
    data = request.json
    rule_ids = data['rule_ids']
    print(rule_ids)
    try:
        for rule_id in rule_ids:
            delete_rule(rule_id)
        return jsonify({"Result": "Rule Delted"}), 200
    except Exception as e:
        print(f"Error during deleting rules: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
