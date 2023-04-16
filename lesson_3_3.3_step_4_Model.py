class Model:
    def __init__(self):
        self.d = {}

    def query(self, **kwargs):
        return self.d.update(kwargs)

    def __str__(self, *args, **kwargs):
        if not self.d:
            return "Model"
        return "Model: " + f'{", ".join(" = ".join((k, str(v))) for k, v in self.d.items())}'


model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)