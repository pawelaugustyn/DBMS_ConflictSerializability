class ConflictOperation(object):
    def __init__(self, op_from, op_to):
        self._from = op_from
        self._to = op_to

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_from(self):
        return self._from

    def get_to(self):
        return self._to

    @staticmethod
    def _is_operation(operation):
        return isinstance(operation, ConflictOperation)
