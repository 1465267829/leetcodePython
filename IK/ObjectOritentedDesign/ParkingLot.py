'''
https://www.educative.io/courses/grokking-the-object-oriented-design-interview/gxM3gRxmr8Z

Requirements:
1.  Parking lot needs to have multiple parking floors
2.  Parking lot needs to have multiple parking spots
3.  Parking spot types:
    a. Compact
    b. Large
    c. Electric Spot
    d. Bike
4.  Payment types:
    a. CC
    b. Cash
5.  Queueing of incoming vehicles in event of parking being full
6.  Timing limit imposition
7.  Admin layer for creating and managing parking lot
8.  REST API for interaction with the classes

Classes:

Design Patterns:

Issues to solve:

Rest APIs:
  Control Path APIs aka admin APIs
  Data Path APIs aka transaction APIs
'''


from abc import ABC, abstractmethod
from enum import Enum
import queue
from typing import NewType


class PayType(Enum):
  CC = 0


class VehicleType(Enum):
  CAR = 0


class ParkingSpotType(Enum):
  COMPACT = 0


class User:
  def __init__(self, vehicle, payment):
    self.vehicle = vehicle
    self.payment = payment
    self.parking_ticket = None

  @property
  def vehicle(self): return self.vehicle

  @vehicle.setter
  def vehicle(self, val):
    self.vehicle = val

  @property
  def payment(self): return self.payment

  @vehicle.setter
  def payment(self, val):
    self.payment = val

  @property
  def parking_ticket(self):
    return self.parking_ticket

  @parking_ticket.setter
  def parking_ticket(self, val):
    self.parking_ticket = val



class ParkingTicket:
  def __init__(self, start_time):
    self.id = None
    self.start_time = start_time
    self.end_time= None
    self.amount = None

  def status(self):
    pass


Receipt = NewType('Receipt', ParkingTicket)


class Payment(ABC):
  def __init__(self, details):
    self.type = None
    self.details = None

  @abstractmethod
  def pay(self):
    None


class CreditCard(Payment):
  def pay(self):
    pass


class Vehicle(ABC):
  @abstractmethod
  def __init__(self, id=None, size=None):
    self._id = id
    self._size = size

  @property
  def id(self): return self._id

  @property
  def size(self): return self._size


class Car(Vehicle):
  def __init__(self, config):
    pass
    super().__init__(config['id'], config['size'])


class ParkingSpot:
  def __init__(self, id, type):
    self._id = id
    self._type = type
    self.vehicle = None

  @property
  def id(self): return self._id

  @property
  def type(self): return self._type


class ParkingFloor:
  def __init__(self, config):
    self._id = config.get('id', None)
    self._capacity = config.get('cap', None)
    self.spots = config['spots']

  @property
  def id(self): return self._id

  @property
  def capacity(self): return self._capacity

  @property
  def spots(self): return self._spots

  @spots.setter
  def spots(self, config):
    # Set spots property to be 'compose'd of ParkingSpot objects
    # Build each spot from parking_lot_config['floors']['spots'] configs
    pass


class ParkingLot:
  def __init__(self, config):
    self._id = config.get('id', None)
    self._addr = config.get('addr', None)
    self.floors = config['floors']
    self.parked = {
    }
    self.available = {
      ParkingSpotType.COMPACT: queue.LifoQueue(maxsize=10),
    }

  @property
  def id(self): return self._id

  @property
  def addr(self): return self._addr

  @property
  def floors(self):
    return self._floors

  @floors.setter
  def floors(self, config):
    # Set floors property to be 'compose'd of ParkingFloor objects
    # Build each floor from parking_lot_config['floors'] configs
    pass

  def park(self, vehicle) -> Receipt:
    # Use command pattern to implement transactions
    # Walk through self.available DS and find a suitable empty spot

    # If found an empty suitable spot:
      # 1. Remove the ParkingSpot from self.available
      # 2. Fill the spot with vehicle object
      # 3. Create a receipt object
      # 4. Update the self.parked with key as receipt id and value as spot object and receipt object
      # 4. Return the receipt object
    # Else raise an exception for user to manage it [TODO: Introduce a queue]
    pass

  def unpark(self, receipt, payment) -> Receipt:
    # Use command pattern to implement transactions
    # From receipt object get the received id
    # Fetch the receipt object and spot object from self.parked
    # Calculate the amount due taking into account the time elapsed and slot type
    # Update the ticket with amount
    # Invoke payment method to to pay the amount in the ticket
    # Set the Parking Spot vehicle to None
    # Move the vehicle to self.available appropriate List
    # Return the ticket object
    pass


if __name__ == '__main__':
  car_details = None
  car = Car(car_details)
  payment_details = None
  credit_card = CreditCard(payment_details)
  user = User(car, credit_card)

  parking_lot_config = {
    'id': 0,
    'addr': 'pl_addr',
    'floors': [
      {'id': 0, 'cap': 2, 'spots': [{id:0, type:0}, {id:1, type:1}]},
      {'id': 1, 'cap': 2, 'spots': [{id:0, type:0}, {id:1, type:1}]},
    ]
  }

  parking_lot = ParkingLot(parking_lot_config)
  parking_ticket = parking_lot.park(user.vehicle)
  paid_parking_ticket = parking_lot.unpark(parking_ticket, user.payment)
