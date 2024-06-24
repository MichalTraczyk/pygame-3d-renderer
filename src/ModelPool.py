class ModelPool:
    pool = []
    listeners = []

    @classmethod
    def add_change_listener(cls,listener):
        cls.listeners.append(listener)
    @classmethod
    def register_model(cls, model):
        cls.pool.append(model)
        for listener in cls.listeners:
            listener(cls.pool)
    @classmethod
    def unregister_model(cls,model):
        cls.pool.remove(model)
        for listener in cls.listeners:
            listener(cls.pool)