import json
import os

from app.schemas.task import createTeam


# DB_File = "../data/tasks.json"
# DB_File = "data/tasks.json"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # current file ka folder
DB_File = os.path.normpath(os.path.join(BASE_DIR, "..", "data", "tasks.json"))


class TeamManager :
    def __init__(self):
        
        db_folder = os.path.dirname(DB_File)
        if not os.path.exists(db_folder):
            os.makedirs(db_folder)
        
        if not os.path.exists(DB_File):
            with open(DB_File, "w") as f:
                json.dump({}, f , indent=4)

    def _read_team(self) -> dict:
        with open(DB_File, "r") as f:
            return json.load(f)

    def _write_teams(self, data: dict):
        with open(DB_File, "w") as f:
            json.dump(data, f, indent=4)

    
    def get_user(self, user_id: str) -> dict:
        """
        Returns user info based on user_id
        """
        users = self._read_team()
        if user_id not in users:
            return {"error": "User not found."}
        return users[user_id]
    
    # def _get_next_id(self, teams):
    #     if not teams:
    #         return "1"
        
    #     last_id = max(int(t["id"]) for t in teams.values())
    #     return str(last_id + 1)
    def _get_next_id(self, teams):
        if not teams:
            return "1"

        valid_ids = [int(t.get("id", 0)) for t in teams.values() if "id" in t]
        if not valid_ids:
            return "1"

        last_id = max(valid_ids)
        return str(last_id + 1)


    def create_team(self, team_data: createTeam) -> dict:
        teams = self._read_team()
        team_id = self._get_next_id(teams)

        teams[team_id] = {
            "id": team_id, 
            "date": str(team_data.date),
            "entity_name": team_data.entity_name,
            "task_type": team_data.task_type,
            "time": str(team_data.time),
            "contact_id": team_data.contact_person,
            "note": team_data.note,
            "status": team_data.status
        }

        self._write_teams(teams)

        return {"message": "User created successfully", "user": teams[team_id]}


    def get_all_users(self) -> dict:
        """Returns all user details"""
        return self._read_team()
    
    def get_team_by_id(self, team_id: str) -> dict:
        data = self._read_team()
        print("data",)
        for team in data.values():
            if str(team["id"]) == str(team_id):
                return {"message": "Team found", "user": team}
        return {"message": f"Team with id {team_id} not found"}
    

    def update_team1(self, team_id: str, new_data: dict) -> dict:
        team = self._read_team()   # yeh ek list of dicts hai
        print("new", new_data)
        team[team_id]["entity_name"] = new_data["entity_name"]
        team[team_id]["task_type"] = new_data["task_type"]
        team[team_id]["contact_id"] = new_data["contact_id"]
        team[team_id]["note"] = new_data["note"]
        team[team_id]["status"] = new_data["status"]

                # write back to JSON
        self._write_teams(team)

        return {"message": "Team updated successfully", "user": team}

        

    def update_team(self, team_id: str, new_data: dict) -> dict:
        teams = self._read_team()   # dict of dicts
        
        if str(team_id) not in teams:
            return {"message": f"Team with id {team_id} not found"}

        # sirf update hone wale fields (date/time ko skip karenge)
        skip_fields = ["id", "date", "time"]
        for key, value in new_data.items():
            if key not in skip_fields:
                teams[team_id][key] = value

        # write back to JSON
        self._write_teams(teams)

        return {"message": "Team updated successfully", "user": teams[team_id]} 
    

    def update_status(self, team_id: str, new_status: str) -> dict:
        data = self._read_team()  # dict of dicts

        if str(team_id) in data:
            team = data[str(team_id)]
            team["status"] = new_status  # sirf status update karega

            data[str(team_id)] = team
            self._write_teams(data)

            return {"message": "Status updated successfully", "user": team}

        return {"message": f"Team with id {team_id} not found"} 

    def delete_team(self, team_id: str) -> dict:
        data = self._read_team()  # dict of dicts

        if str(team_id) in data:
            deleted_team = data.pop(str(team_id))  # remove entry
            self._write_teams(data)
            return {"message": "Team deleted successfully", "deleted_user": deleted_team}

        return {"message": f"Team with id {team_id} not found"}
