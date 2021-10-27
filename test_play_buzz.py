from ChoiceType import ChoiceType
from PlayBuzzManager import PlayBuzzManager, Result


class TestPlayBuzz:
    def setup_can_you_pass_this_tricky_eye_test(self, test_name):
        self.play_buzz_manager = PlayBuzzManager(
            "https://www.playbuzz.com/jessicafavish10/can-you-pass-this-tricky-eye-test", test_name)

    def base_test(self, test_name, choices):
        self.setup_can_you_pass_this_tricky_eye_test(test_name)
        result = self.play_buzz_manager.make_choices(choices)
        self.play_buzz_manager.save_screenshot()
        return result

    def test_fail(self):
        result: Result = self.base_test("test_fail", [ChoiceType.First] * 9)
        assert result.title == "Oh No!"

    def test_success1(self):  # 7 out of 9 is correct
        result: Result = self.base_test("test_success1", [
            ChoiceType.Third, ChoiceType.Second, ChoiceType.Third,
            ChoiceType.First, ChoiceType.First, ChoiceType.Second,
            ChoiceType.Third, ChoiceType.Third, ChoiceType.Third])
        assert result.title == "Dot Master!!"

    def test_max_score(self):
        result: Result = self.base_test("test_max_score", [
            ChoiceType.Third, ChoiceType.Second, ChoiceType.Third,
            ChoiceType.First, ChoiceType.First, ChoiceType.Second,
            ChoiceType.Third, ChoiceType.Second, ChoiceType.First])
        assert result.title == "Dot Master!!"

    def teardown(self):
        self.play_buzz_manager.quit()
