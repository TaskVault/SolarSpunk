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

from abc import ABC
from typing import Generator, Set, Type, cast

from packages.valory.skills.abstract_round_abci.base import AbstractRound
from packages.valory.skills.abstract_round_abci.behaviours import (
    AbstractRoundBehaviour,
    BaseBehaviour,
)

from packages.zarathustra.skills.solar_spunk_abci.models import Params
from packages.zarathustra.skills.solar_spunk_abci.rounds import (
    SynchronizedData,
    SolarSpunkAbciApp,
    AdjustMiningRateRound,
    CollateralizationRound,
    DataCollectionRound,
    SubscriptionManagementRound,
    UpdateNFTRound,
    YieldFarmingRound,
)
from packages.zarathustra.skills.solar_spunk_abci.rounds import (
    AdjustMiningRatePayload,
    CollateralizationPayload,
    DataCollectionPayload,
    SubscriptionManagementPayload,
    UpdateNFTPayload,
    YieldFarmingPayload,
)


class SolarSpunkBaseBehaviour(BaseBehaviour, ABC):
    """Base behaviour for the solar_spunk_abci skill."""

    @property
    def synchronized_data(self) -> SynchronizedData:
        """Return the synchronized data."""
        return cast(SynchronizedData, super().synchronized_data)

    @property
    def params(self) -> Params:
        """Return the params."""
        return cast(Params, super().params)


class AdjustMiningRateBehaviour(SolarSpunkBaseBehaviour):
    """AdjustMiningRateBehaviour"""

    matching_round: Type[AbstractRound] = AdjustMiningRateRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = AdjustMiningRatePayload(sender=sender, content=...)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class CollateralizationBehaviour(SolarSpunkBaseBehaviour):
    """CollateralizationBehaviour"""

    matching_round: Type[AbstractRound] = CollateralizationRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = CollateralizationPayload(sender=sender, content=...)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class DataCollectionBehaviour(SolarSpunkBaseBehaviour):
    """DataCollectionBehaviour"""

    matching_round: Type[AbstractRound] = DataCollectionRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = DataCollectionPayload(sender=sender, content=...)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class SubscriptionManagementBehaviour(SolarSpunkBaseBehaviour):
    """SubscriptionManagementBehaviour"""

    matching_round: Type[AbstractRound] = SubscriptionManagementRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = SubscriptionManagementPayload(sender=sender, content=...)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class UpdateNFTBehaviour(SolarSpunkBaseBehaviour):
    """UpdateNFTBehaviour"""

    matching_round: Type[AbstractRound] = UpdateNFTRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = UpdateNFTPayload(sender=sender, content=...)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class YieldFarmingBehaviour(SolarSpunkBaseBehaviour):
    """YieldFarmingBehaviour"""

    matching_round: Type[AbstractRound] = YieldFarmingRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = YieldFarmingPayload(sender=sender, content=...)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class SolarSpunkRoundBehaviour(AbstractRoundBehaviour):
    """SolarSpunkRoundBehaviour"""

    initial_behaviour_cls = SubscriptionManagementBehaviour
    abci_app_cls = SolarSpunkAbciApp  # type: ignore
    behaviours: Set[Type[BaseBehaviour]] = [
        AdjustMiningRateBehaviour,
        CollateralizationBehaviour,
        DataCollectionBehaviour,
        SubscriptionManagementBehaviour,
        UpdateNFTBehaviour,
        YieldFarmingBehaviour
    ]
