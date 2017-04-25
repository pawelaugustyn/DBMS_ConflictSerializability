from Operation import Operation
from ConflictOperation import ConflictOperation


class Schedule(object):
    def __init__(self, schedule):
        self._scheduleList = []
        if not self._is_string(schedule):
            raise ValueError("Wrong type")
        operations = schedule.split()
        for op in operations:
            if len(op) != 3:
                raise KeyError
            try:
                insert = Operation(op[0], int(op[1]), op[2])
            except ValueError:
                exit(-1)
            self._scheduleList.append(insert)

    def get_printable_schedule(self):
        result = ""
        for operation in self._scheduleList:
            result += operation.get_operation() + str(operation.get_tid()) + operation.get_var() + " "
        return result

    def is_conflict_serializable(self):
        conflicts = self._create_precedence_graph()
        for outer in conflicts:
            outerFrom = outer.get_from()
            outerTo = outer.get_to()
            for inner in conflicts:
                innerFrom = inner.get_from()
                innerTo = inner.get_to()
                if outerFrom == innerTo and outerTo == innerFrom:
                    return False
        return True

    def _create_precedence_graph(self):
        conflicts = []
        for i in range(0, len(self._scheduleList)):
            outOp = self._scheduleList[i]
            for j in range(0, len(self._scheduleList)):
                inOp = self._scheduleList[j]
                if outOp == inOp:
                    continue
                if outOp.get_operation() == "r" == inOp.get_operation():
                    continue
                if outOp.get_var() != inOp.get_var():
                    continue
                if i < j:
                    confl_op = ConflictOperation(outOp, inOp)
                    conflicts.append(confl_op)
                elif i > j:
                    confl_op = ConflictOperation(inOp, outOp)
                    conflicts.append(confl_op)
        return conflicts

    @staticmethod
    def _is_string(string):
        return isinstance(string, str)