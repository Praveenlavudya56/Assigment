# class ParkingSpot:
#     def __init__(self, spot_type):
#         self.spot_type = spot_type
#         self.is_empty = True
#         self.is_electric = False

# class ParkingFloor:
#     def __init__(self, floor_num, spot_types):
#         self.floor_num = floor_num
#         self.spots = {spot_type: [] for spot_type in spot_types}

#     def add_spot(self, spot_type, spot_count):
#         for _ in range(spot_count):
#             self.spots[spot_type].append(ParkingSpot(spot_type))

# class ParkingLot:
#     def __init__(self, num_floors, max_capacity, spot_types):
#         self.num_floors = num_floors
#         self.max_capacity = max_capacity
#         self.spot_types = spot_types
#         self.floors = [ParkingFloor(floor_num, spot_types) for floor_num in range(1, num_floors + 1)]
#         self.available_spots = {spot_type: max_capacity // num_floors for spot_type in spot_types}

#     def find_available_spot(self, spot_type):
#         for floor in self.floors:
#             for spot in floor.spots[spot_type]:
#                 if spot.is_empty:
#                     return floor, spot
#         return None, None

#     def park_vehicle(self, spot_type, is_electric):
#         if self.available_spots[spot_type] > 0:
#             floor, spot = self.find_available_spot(spot_type)
#             if floor and spot:
#                 spot.is_empty = False
#                 spot.is_electric = is_electric
#                 self.available_spots[spot_type] -= 1
#                 return True
#         return False

#     def unpark_vehicle(self, spot):
#         if spot.is_empty:
#             return False
#         spot.is_empty = True
#         self.available_spots[spot.spot_type] += 1
#         return True

# class ParkingTicket:
#     def __init__(self, spot_type, is_electric):
#         self.spot_type = spot_type
#         self.is_electric = is_electric

# class ParkingFeeCalculator:
#     def calculate_fee(self, hours_parked):
#         if hours_parked == 1:
#             return 4.0
#         elif hours_parked <= 3:
#             return 3.5 * hours_parked
#         else:
#             return 2.5 * hours_parked

# class ParkingSystem:
#     def __init__(self, num_floors, max_capacity, spot_types):
#         self.parking_lot = ParkingLot(num_floors, max_capacity, spot_types)
#         self.ticket_machine = {}

#     def generate_ticket(self, spot_type, is_electric):
#         if self.parking_lot.park_vehicle(spot_type, is_electric):
#             ticket = ParkingTicket(spot_type, is_electric)
#             self.ticket_machine[id(ticket)] = ticket
#             return ticket
#         return None

#     def pay_ticket(self, ticket_id, hours_parked):
#         if ticket_id in self.ticket_machine:
#             ticket = self.ticket_machine[ticket_id]
#             fee_calculator = ParkingFeeCalculator()
#             fee = fee_calculator.calculate_fee(hours_parked)
#             del self.ticket_machine[ticket_id]
#             return fee
#         return None

#     def charge_electric_vehicle(self, spot_type, hours_charged):
#         fee_calculator = ParkingFeeCalculator()
#         fee = fee_calculator.calculate_fee(hours_charged)
#         return fee

# # Sample usage
# parking_system = ParkingSystem(num_floors=3, max_capacity=50, spot_types=["Compact", "Large", "Electric"])

# # Generate a parking ticket
# ticket = parking_system.generate_ticket(spot_type="Compact", is_electric=False)
# if ticket:
#     print("Parking ticket generated.")

# # Simulate payment and departure
# hours_parked = 2
# fee = parking_system.pay_ticket(id(ticket), hours_parked)
# if fee is not None:
#     print(f"Payment successful. Fee: ${fee:.2f}")

# # Charging an electric vehicle
# electric_fee = parking_system.charge_electric_vehicle(spot_type="Electric", hours_charged=3)
# print(f"Electric vehicle charging fee: ${electric_fee:.2f}")


import datetime

class ParkingLot:
    def __init__(self, num_floors, max_capacity_per_floor):
        self.num_floors = num_floors
        self.max_capacity_per_floor = max_capacity_per_floor
        self.floors = []

    def add_floor(self, floor):
        if len(self.floors) < self.num_floors:
            self.floors.append(floor)
        else:
            print("Cannot add more floors, parking lot is full.")

    def is_full(self):
        return all(floor.is_full() for floor in self.floors)

class Floor:
    def __init__(self, floor_number, num_spots_per_type):
        self.floor_number = floor_number
        self.num_spots_per_type = num_spots_per_type
        self.spots = {spot_type: [] for spot_type in Spot.SPOT_TYPES}

    def add_spot(self, spot):
        if len(self.spots[spot.spot_type]) < self.num_spots_per_type:
            self.spots[spot.spot_type].append(spot)
        else:
            print(f"No more {spot.spot_type} spots available on floor {self.floor_number}.")

    def is_full(self):
        return all(len(spots) >= self.num_spots_per_type for spots in self.spots.values())

class Spot:
    SPOT_TYPES = ["Compact", "Large"]  # Add more spot types as needed

    def __init__(self, spot_number, spot_type):
        self.spot_number = spot_number
        self.spot_type = spot_type
        self.is_empty = True

class Ticket:
    def __init__(self, spot, entry_time):
        self.spot = spot
        self.entry_time = entry_time

    def calculate_fee(self, exit_time):
        time_difference = exit_time - self.entry_time
        hours_parked = time_difference.total_seconds() / 3600

        fee_structure = [(1, 4), (3, 3.5), (None, 2.5)]
        fee = 0
        for limit, rate in fee_structure:
            if limit is None or hours_parked <= limit:
                fee += (hours_parked if limit is None else limit) * rate
                break

        return fee

class Payment:
    PAYMENT_METHODS = ["cash", "credit_card"]

    def process_payment(self, amount, payment_method):
        if payment_method in self.PAYMENT_METHODS:
            print(f"{payment_method.capitalize()} payment successful. Amount: {amount:.2f}")
            return True
        else:
            print("Invalid payment method.")
            return False

class ElectricPanel:
    def process_payment_and_charge(self, ticket, exit_time):
        fee = ticket.calculate_fee(exit_time)
        
        payment = Payment()
        payment_successful = payment.process_payment(fee, "credit_card")
        
        if payment_successful:
            print("Electric car charged successfully.")
        else:
            print("Payment or charging failed.")

# Example usage:
def main():
    parking_lot = ParkingLot(num_floors=3, max_capacity_per_floor=50)
    floor1 = Floor(floor_number=1, num_spots_per_type=20)
    floor2 = Floor(floor_number=2, num_spots_per_type=30)
    parking_lot.add_floor(floor1)
    parking_lot.add_floor(floor2)

    spot1 = Spot(spot_number=1, spot_type="Compact")
    entry_time = datetime.datetime(2023, 8, 10, 10, 0, 0)
    exit_time = datetime.datetime(2023, 8, 10, 12, 30, 0)
    ticket = Ticket(spot=spot1, entry_time=entry_time)
    fee = ticket.calculate_fee(exit_time)
    print(f"Total fee: {fee:.2f}")

    payment = Payment()
    payment.process_payment(fee, "cash")

    electric_panel = ElectricPanel()
    electric_panel.process_payment_and_charge(ticket, exit_time)

if __name__ == "__main__":
    main()
