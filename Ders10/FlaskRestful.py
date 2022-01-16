import flask
import flask_restful

app = flask.Flask(__name__)
api = flask_restful.Api(app)

todo = {
    1: {'task': 'Pencereyi ac'},
    2: {'task': 'Perdeyi arala'},
    3: {'task': 'Odevi yap'}
}

class Todo(flask_restful.Resource):
    def get(self, todo_id):
        flask.request.
        if todo_id not in todo.keys():
            flask_restful.abort(404, message = f"Cannot find todo item with id {todo_id}")
        return todo[todo_id]

    def delete(self, todo_id):
        task = todo[todo_id]
        del todo[todo_id]
        return task

    def put(self, todo_id):
        todo[todo_id] = {'task': flask.request.form['task']}
        return todo[todo_id]

class TodoList(flask_restful.Resource):
    def get(self):
        return todo

    def post(self):
        var = flask.request.form.getlist('task')
        for item in var:
            tid = len(todo.keys()) + 1
            todo[tid] = {'task': item}

        return todo

api.add_resource(TodoList,"/todos")
api.add_resource(Todo, "/todo/<int:todo_id>")

app.run()