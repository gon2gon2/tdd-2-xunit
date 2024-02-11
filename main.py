class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
            print(method)
        self.tearDown()

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


# test for
class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


class TestCaseTest(TestCase):
    def __init__(self, name):
        super().__init__(name)

    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert ("setUp testMethod tearDown" == self.test.log)

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert ("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(result)
        assert ("1 run, 1 failed" == result.summary())

    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert ("1 run, 1 failed" == result.summary())

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        result = suite.run()
        assert ("2 run, 1 failed" == result.summary())


if __name__ == "__main__":
    suite = TestSuite()
    suite.add(TestCaseTest("testTemplateMethod"))
    suite.add(TestCaseTest("testResult"))
    suite.add(TestCaseTest("testFailedResult"))
    suite.add(TestCaseTest("testFailedResultFormatting"))
    suite.add(TestCaseTest("testSuite"))
    result = TestResult()
    suite.run(result)
    print(result.summary())
