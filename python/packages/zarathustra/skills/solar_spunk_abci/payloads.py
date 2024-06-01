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

"""This module contains the transaction payloads of the SolarSpunkAbciApp."""

from dataclasses import dataclass

from packages.valory.skills.abstract_round_abci.base import BaseTxPayload


@dataclass(frozen=True)
class AdjustMiningRatePayload(BaseTxPayload):
    """Represent a transaction payload for the AdjustMiningRateRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class CollateralizationPayload(BaseTxPayload):
    """Represent a transaction payload for the CollateralizationRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class DataCollectionPayload(BaseTxPayload):
    """Represent a transaction payload for the DataCollectionRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class SubscriptionManagementPayload(BaseTxPayload):
    """Represent a transaction payload for the SubscriptionManagementRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class UpdateNFTPayload(BaseTxPayload):
    """Represent a transaction payload for the UpdateNFTRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class YieldFarmingPayload(BaseTxPayload):
    """Represent a transaction payload for the YieldFarmingRound."""

    # TODO: define your attributes

