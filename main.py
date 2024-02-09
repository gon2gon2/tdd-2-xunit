class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        self.wasSetUp = None
        self.wasRun = None
        self.log = ""
        super().__init__(name)

    def setUp(self):
        self.log += "setUp "
        self.wasSetUp = 1

    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "


class TestCaseTest(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.test = None

    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert self.test.wasRun

    def testSetUp(self):
        self.test.run()
        assert ("setUp testMethod " == self.test.log)


if __name__ == "__main__":
    TestCaseTest("testRunning").run()
    TestCaseTest("testSetUp").run()
