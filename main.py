class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        testResult = TestResult()
        testResult.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return testResult

    def tearDown(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        self.log = ""
        super().__init__(name)

    def setUp(self):
        self._addLog("setUp")

    def testMethod(self):
        self._addLog("testMethod")

    def tearDown(self):
        self._addLog("tearDown")

    def _addLog(self, log):
        if self.log == "":
            self.log = log
            return

        self.log = self.log + " " + log

class TestResult:
    def __init__(self):
        self.runCount = 0

    def testStarted(self):
        self.runCount = self.runCount + 1

    def summary(self):
        return f"{self.runCount} run, 0 failed"


# test for
class TestCaseTest(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.test = None

    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert ("setUp testMethod tearDown" == self.test.log)

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert ("1 run, 0 failed" == result.summary())


if __name__ == "__main__":
    TestCaseTest("testTemplateMethod").run()
    TestCaseTest("testResult").run()
