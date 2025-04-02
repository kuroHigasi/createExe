import pygame
import pygame.locals
import system.action as testAction
import system.status as testStatus
import system.form as testForm
# FORM
import common.operation.form as operationForm
import system.form as systemForm
import common.status.form as statusForm
# DEFINE
import common.pyd.status as STATUS
import pytest

@pytest.fixture
def setup():
    # Initialize Pygame
    pygame.init()


class TestAction():
    def test_HOME_0(self, setup):
        testOpeForm = operationForm.OperationForm()
        testSysForm = systemForm.SystemForm()
        testStaForm = statusForm.Form(STATUS.HOME())
        testAction.Action.execute(testStaForm, testSysForm, testOpeForm)
        assert testStaForm.NOW_STATUS() is STATUS.HOME()
        assert testStaForm.PRE_STATUS() is STATUS.HOME()

    def test_CONFIG_0(self, setup):
        testOpeForm = operationForm.OperationForm()
        testSysForm = systemForm.SystemForm()
        testStaForm = statusForm.Form(STATUS.CONFIG())
        testAction.Action.execute(testStaForm, testSysForm, testOpeForm)
        assert testStaForm.NOW_STATUS() is STATUS.CONFIG()
        assert testStaForm.PRE_STATUS() is STATUS.CONFIG()

    def test_DUNGEON_0(self, setup):
        testOpeForm = operationForm.OperationForm()
        testSysForm = systemForm.SystemForm()
        testStaForm = statusForm.Form(STATUS.DUNGEON())
        testAction.Action.execute(testStaForm, testSysForm, testOpeForm)
        assert testStaForm.NOW_STATUS() is STATUS.DUNGEON()
        assert testStaForm.PRE_STATUS() is STATUS.DUNGEON()

class TestStatus():
    def test_HOME_0(self, setup):
        testOpeForm = operationForm.OperationForm()
        testSysForm = systemForm.SystemForm()
        testStaForm = statusForm.Form(STATUS.HOME())
        testStatus.Status.execute(testStaForm, testSysForm, testOpeForm)
        assert testStaForm.NOW_STATUS() is STATUS.HOME()
        assert testStaForm.PRE_STATUS() is STATUS.HOME()

    def test_CONFIG_0(self, setup):
        testOpeForm = operationForm.OperationForm()
        testSysForm = systemForm.SystemForm()
        testStaForm = statusForm.Form(STATUS.CONFIG())
        testStatus.Status.execute(testStaForm, testSysForm, testOpeForm)
        assert testStaForm.NOW_STATUS() is STATUS.CONFIG()
        assert testStaForm.PRE_STATUS() is STATUS.CONFIG()

    def test_DUNGEON_0(self, setup):
        testOpeForm = operationForm.OperationForm()
        testSysForm = systemForm.SystemForm()
        testStaForm = statusForm.Form(STATUS.DUNGEON())
        testStatus.Status.execute(testStaForm, testSysForm, testOpeForm)
        assert testStaForm.NOW_STATUS() is STATUS.DUNGEON()
        assert testStaForm.PRE_STATUS() is STATUS.DUNGEON()
