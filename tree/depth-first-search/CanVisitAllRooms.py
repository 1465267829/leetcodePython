'''
https://leetcode.com/problems/keys-and-rooms/
841. Keys and Rooms
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room.

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0).

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
Note:

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.
'''
class Solution(object):
  def canVisitAllRooms(self, rooms):
    """
    :type rooms: List[List[int]]
    :rtype: bool
    """
    if not rooms: return False

    room_visit_tracker = []
    for _ in range(len(rooms)):
      # Mark each room in room_visit_tracker as unvisted (0)
      room_visit_tracker.append(0)

    next_rooms_to_visit_indices = []
    current_room_index = 0
    next_rooms_to_visit_indices.append(current_room_index)

    while next_rooms_to_visit_indices:
      current_room_index = next_rooms_to_visit_indices.pop(0)
      room_visit_tracker[current_room_index] = 1
      keys_in_current_room = rooms[current_room_index]
      if keys_in_current_room:
        for key in keys_in_current_room:
          if (room_visit_tracker[key] != 1) and (0 <= key < len(rooms)):
            # unvisited room
            next_rooms_to_visit_indices.append(key)
    return all(v is 1 for v in room_visit_tracker)

if __name__ == "__main__":
  rooms = [[1,3],[3,0,1],[2],[0]]
  # rooms = [[1], [2], [3], []]
  sol = Solution()
  print(sol.canVisitAllRooms(rooms))