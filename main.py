class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        testResult = TestResult()
        testResult.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            testResult.testFailed()
        finally:
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

    def testBrokenMethod(self):
        raise Exception


class TestResult:
    def __init__(self):
        self.runCount = 0
        self.failureCount = 0

    def testStarted(self):
        self.runCount += 1

    def summary(self):
        return f"{self.runCount} run, {self.failureCount} failed"

    def testFailed(self):
        self.failureCount += 1


class TestCaseTest(TestCase):
    def __init__(self, name):
        super().__init__(name)

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert ("setUp testMethod tearDown" == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert ("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert ("1 run, 1 failed" == result.summary())

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert ("1 run, 1 failed" == result.summary())


if __name__ == "__main__":
    print(TestCaseTest("testTemplateMethod").run().summary())
    print(TestCaseTest("testResult").run().summary())
    print(TestCaseTest("testFailedResult").run().summary())
    print(TestCaseTest("testFailedResultFormatting").run().summary())
