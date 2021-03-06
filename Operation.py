class Operation(object):
    def __init__(self, op, t_id, var):
        self._operation = op
        self._transactionID = t_id
        self._variableName = var

    def get_operation(self):
        return self._operation

    def get_tid(self):
        return self._transactionID

    def get_var(self):
        return self._variableName

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Operation):
            return False
        return self._transactionID == other.get_tid()

    @staticmethod
    def _is_operation(operation):
        return isinstance(operation, Operation)