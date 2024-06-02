import { newMockEvent } from "matchstick-as"
import { ethereum, Address, BigInt } from "@graphprotocol/graph-ts"
import {
  Approval,
  ApprovalForAll,
  HourlyPowerConsumption,
  HourlyPowerProduction,
  NewSpunkerJoined,
  OwnershipTransferred,
  Transfer
} from "../generated/SolarSpunkerNFT/SolarSpunkerNFT"

export function createApprovalEvent(
  owner: Address,
  approved: Address,
  tokenId: BigInt
): Approval {
  let approvalEvent = changetype<Approval>(newMockEvent())

  approvalEvent.parameters = new Array()

  approvalEvent.parameters.push(
    new ethereum.EventParam("owner", ethereum.Value.fromAddress(owner))
  )
  approvalEvent.parameters.push(
    new ethereum.EventParam("approved", ethereum.Value.fromAddress(approved))
  )
  approvalEvent.parameters.push(
    new ethereum.EventParam(
      "tokenId",
      ethereum.Value.fromUnsignedBigInt(tokenId)
    )
  )

  return approvalEvent
}

export function createApprovalForAllEvent(
  owner: Address,
  operator: Address,
  approved: boolean
): ApprovalForAll {
  let approvalForAllEvent = changetype<ApprovalForAll>(newMockEvent())

  approvalForAllEvent.parameters = new Array()

  approvalForAllEvent.parameters.push(
    new ethereum.EventParam("owner", ethereum.Value.fromAddress(owner))
  )
  approvalForAllEvent.parameters.push(
    new ethereum.EventParam("operator", ethereum.Value.fromAddress(operator))
  )
  approvalForAllEvent.parameters.push(
    new ethereum.EventParam("approved", ethereum.Value.fromBoolean(approved))
  )

  return approvalForAllEvent
}

export function createHourlyPowerConsumptionEvent(
  user: Address,
  consumption: BigInt
): HourlyPowerConsumption {
  let hourlyPowerConsumptionEvent = changetype<HourlyPowerConsumption>(
    newMockEvent()
  )

  hourlyPowerConsumptionEvent.parameters = new Array()

  hourlyPowerConsumptionEvent.parameters.push(
    new ethereum.EventParam("user", ethereum.Value.fromAddress(user))
  )
  hourlyPowerConsumptionEvent.parameters.push(
    new ethereum.EventParam(
      "consumption",
      ethereum.Value.fromUnsignedBigInt(consumption)
    )
  )

  return hourlyPowerConsumptionEvent
}

export function createHourlyPowerProductionEvent(
  user: Address,
  production: BigInt
): HourlyPowerProduction {
  let hourlyPowerProductionEvent = changetype<HourlyPowerProduction>(
    newMockEvent()
  )

  hourlyPowerProductionEvent.parameters = new Array()

  hourlyPowerProductionEvent.parameters.push(
    new ethereum.EventParam("user", ethereum.Value.fromAddress(user))
  )
  hourlyPowerProductionEvent.parameters.push(
    new ethereum.EventParam(
      "production",
      ethereum.Value.fromUnsignedBigInt(production)
    )
  )

  return hourlyPowerProductionEvent
}

export function createNewSpunkerJoinedEvent(user: Address): NewSpunkerJoined {
  let newSpunkerJoinedEvent = changetype<NewSpunkerJoined>(newMockEvent())

  newSpunkerJoinedEvent.parameters = new Array()

  newSpunkerJoinedEvent.parameters.push(
    new ethereum.EventParam("user", ethereum.Value.fromAddress(user))
  )

  return newSpunkerJoinedEvent
}

export function createOwnershipTransferredEvent(
  previousOwner: Address,
  newOwner: Address
): OwnershipTransferred {
  let ownershipTransferredEvent = changetype<OwnershipTransferred>(
    newMockEvent()
  )

  ownershipTransferredEvent.parameters = new Array()

  ownershipTransferredEvent.parameters.push(
    new ethereum.EventParam(
      "previousOwner",
      ethereum.Value.fromAddress(previousOwner)
    )
  )
  ownershipTransferredEvent.parameters.push(
    new ethereum.EventParam("newOwner", ethereum.Value.fromAddress(newOwner))
  )

  return ownershipTransferredEvent
}

export function createTransferEvent(
  from: Address,
  to: Address,
  tokenId: BigInt
): Transfer {
  let transferEvent = changetype<Transfer>(newMockEvent())

  transferEvent.parameters = new Array()

  transferEvent.parameters.push(
    new ethereum.EventParam("from", ethereum.Value.fromAddress(from))
  )
  transferEvent.parameters.push(
    new ethereum.EventParam("to", ethereum.Value.fromAddress(to))
  )
  transferEvent.parameters.push(
    new ethereum.EventParam(
      "tokenId",
      ethereum.Value.fromUnsignedBigInt(tokenId)
    )
  )

  return transferEvent
}
