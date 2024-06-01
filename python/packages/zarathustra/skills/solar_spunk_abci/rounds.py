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

"""This package contains the rounds of SolarSpunkAbciApp."""

from enum import Enum
from typing import Dict, FrozenSet, List, Optional, Set, Tuple

from packages.valory.skills.abstract_round_abci.base import (
    AbciApp,
    AbciAppTransitionFunction,
    AbstractRound,
    AppState,
    BaseSynchronizedData,
    DegenerateRound,
    EventToTimeout,
)

from packages.zarathustra.skills.solar_spunk_abci.payloads import (
    AdjustMiningRatePayload,
    CollateralizationPayload,
    DataCollectionPayload,
    SubscriptionManagementPayload,
    UpdateNFTPayload,
    YieldFarmingPayload,
)


class Event(Enum):
    """SolarSpunkAbciApp Events"""

    NO_MAJORITY = "no_majority"
    TIMEOUT = "timeout"
    DONE = "done"


class SynchronizedData(BaseSynchronizedData):
    """
    Class to represent the synchronized data.

    This data is replicated by the tendermint application.
    """


class AdjustMiningRateRound(AbstractRound):
    """AdjustMiningRateRound"""

    payload_class = AdjustMiningRatePayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: AdjustMiningRatePayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: AdjustMiningRatePayload) -> None:
        """Process payload."""
        raise NotImplementedError


class CollateralizationRound(AbstractRound):
    """CollateralizationRound"""

    payload_class = CollateralizationPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: CollateralizationPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: CollateralizationPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class DataCollectionRound(AbstractRound):
    """DataCollectionRound"""

    payload_class = DataCollectionPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: DataCollectionPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: DataCollectionPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class SubscriptionManagementRound(AbstractRound):
    """SubscriptionManagementRound"""

    payload_class = SubscriptionManagementPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: SubscriptionManagementPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: SubscriptionManagementPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class UpdateNFTRound(AbstractRound):
    """UpdateNFTRound"""

    payload_class = UpdateNFTPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: UpdateNFTPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: UpdateNFTPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class YieldFarmingRound(AbstractRound):
    """YieldFarmingRound"""

    payload_class = YieldFarmingPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: YieldFarmingPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: YieldFarmingPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class TransactionSubmissionRound(DegenerateRound):
    """TransactionSubmissionRound"""


class SolarSpunkAbciApp(AbciApp[Event]):
    """SolarSpunkAbciApp"""

    initial_round_cls: AppState = SubscriptionManagementRound
    initial_states: Set[AppState] = {SubscriptionManagementRound}
    transition_function: AbciAppTransitionFunction = {
        SubscriptionManagementRound: {
            Event.DONE: DataCollectionRound,
            Event.NO_MAJORITY: SubscriptionManagementRound,
            Event.TIMEOUT: SubscriptionManagementRound
        },
        DataCollectionRound: {
            Event.DONE: AdjustMiningRateRound,
            Event.NO_MAJORITY: DataCollectionRound,
            Event.TIMEOUT: SubscriptionManagementRound
        },
        AdjustMiningRateRound: {
            Event.DONE: UpdateNFTRound,
            Event.NO_MAJORITY: AdjustMiningRateRound,
            Event.TIMEOUT: SubscriptionManagementRound
        },
        UpdateNFTRound: {
            Event.DONE: CollateralizationRound,
            Event.NO_MAJORITY: UpdateNFTRound,
            Event.TIMEOUT: SubscriptionManagementRound
        },
        CollateralizationRound: {
            Event.DONE: YieldFarmingRound,
            Event.NO_MAJORITY: CollateralizationRound,
            Event.TIMEOUT: SubscriptionManagementRound
        },
        YieldFarmingRound: {
            Event.DONE: TransactionSubmissionRound,
            Event.NO_MAJORITY: YieldFarmingRound,
            Event.TIMEOUT: SubscriptionManagementRound
        },
        TransactionSubmissionRound: {}
    }
    final_states: Set[AppState] = {TransactionSubmissionRound}
    event_to_timeout: EventToTimeout = {}
    cross_period_persisted_keys: FrozenSet[str] = frozenset()
    db_pre_conditions: Dict[AppState, Set[str]] = {
        SubscriptionManagementRound: {'participants'},
    }
    db_post_conditions: Dict[AppState, Set[str]] = {
        TransactionSubmissionRound: {'most_voted_tx_hash'},
    }
