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



