# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2024 zarathustra
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This package contains round behaviours of SolarSpunkAbciApp."""

from pathlib import Path
from typing import Any, Dict, Hashable, Optional, Type
from dataclasses import dataclass, field

import pytest

from packages.valory.skills.abstract_round_abci.base import AbciAppDB
from packages.valory.skills.abstract_round_abci.behaviours import (
    AbstractRoundBehaviour,
    BaseBehaviour,
    make_degenerate_behaviour,
)
from packages.zarathustra.skills.solar_spunk_abci.behaviours import (
    SolarSpunkBaseBehaviour,
    SolarSpunkRoundBehaviour,
    AdjustMiningRateBehaviour,
    CollateralizationBehaviour,
    DataCollectionBehaviour,
    SubscriptionManagementBehaviour,
    UpdateNFTBehaviour,
    YieldFarmingBehaviour,
)
from packages.zarathustra.skills.solar_spunk_abci.rounds import (
    SynchronizedData,
    DegenerateRound,
    Event,
    SolarSpunkAbciApp,
    AdjustMiningRateRound,
    CollateralizationRound,
    DataCollectionRound,
    SubscriptionManagementRound,
    TransactionSubmissionRound,
    UpdateNFTRound,
    YieldFarmingRound,
)

from packages.valory.skills.abstract_round_abci.test_tools.base import (
    FSMBehaviourBaseCase,
)


@dataclass
class BehaviourTestCase:
    """BehaviourTestCase"""

    name: str
    initial_data: Dict[str, Hashable]
    event: Event
    kwargs: Dict[str, Any] = field(default_factory=dict)


class BaseSolarSpunkTest(FSMBehaviourBaseCase):
    """Base test case."""

    path_to_skill = Path(__file__).parent.parent

    behaviour: SolarSpunkRoundBehaviour
    behaviour_class: Type[SolarSpunkBaseBehaviour]
    next_behaviour_class: Type[SolarSpunkBaseBehaviour]
    synchronized_data: SynchronizedData
    done_event = Event.DONE

    @property
    def current_behaviour_id(self) -> str:
        """Current RoundBehaviour's behaviour id"""

        return self.behaviour.current_behaviour.behaviour_id

    def fast_forward(self, data: Optional[Dict[str, Any]] = None) -> None:
        """Fast-forward on initialization"""

        data = data if data is not None else {}
        self.fast_forward_to_behaviour(
            self.behaviour,
            self.behaviour_class.behaviour_id,
            SynchronizedData(AbciAppDB(setup_data=AbciAppDB.data_to_lists(data))),
        )
        assert self.current_behaviour_id == self.behaviour_class.behaviour_id

    def complete(self, event: Event) -> None:
        """Complete test"""

        self.behaviour.act_wrapper()
        self.mock_a2a_transaction()
        self._test_done_flag_set()
        self.end_round(done_event=event)
        assert self.current_behaviour_id == self.next_behaviour_class.behaviour_id


class TestAdjustMiningRateBehaviour(BaseSolarSpunkTest):
    """Tests AdjustMiningRateBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = AdjustMiningRateBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestCollateralizationBehaviour(BaseSolarSpunkTest):
    """Tests CollateralizationBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = CollateralizationBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestDataCollectionBehaviour(BaseSolarSpunkTest):
    """Tests DataCollectionBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = DataCollectionBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestSubscriptionManagementBehaviour(BaseSolarSpunkTest):
    """Tests SubscriptionManagementBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = SubscriptionManagementBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestUpdateNFTBehaviour(BaseSolarSpunkTest):
    """Tests UpdateNFTBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = UpdateNFTBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestYieldFarmingBehaviour(BaseSolarSpunkTest):
    """Tests YieldFarmingBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = YieldFarmingBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)

