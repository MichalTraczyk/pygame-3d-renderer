class ModelPool:
    __pool = []
    __listeners = []

    @classmethod
    def add_change_listener(cls, listener):
        """
        Adds listener that listens when a model pool changes
        @param listener: Method to call when the model pool changes
        """
        cls.__listeners.append(listener)

    @classmethod
    def register_model(cls, model):
        """
        Adds model to model pool
        @param model: Model to add
        """
        cls.__pool.append(model)
        for listener in cls.__listeners:
            listener(cls.__pool)

    @classmethod
    def unregister_model(cls, model):
        """
        Removes model from the model pool
        @param model: Model to remove
        """
        cls.__pool.remove(model)
        for listener in cls.__listeners:
            listener(cls.__pool)
