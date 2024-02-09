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
        self.log = ""
        super().__init__(name)

    def setUp(self):
        self.log += "setUp "

    def testMethod(self):
        self.log = self.log + "testMethod "


class TestCaseTest(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.test = None

    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert ("setUp testMethod " == self.test.log)


if __name__ == "__main__":
    TestCaseTest("testTemplateMethod").run()
