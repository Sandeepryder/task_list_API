from fastapi import APIRouter
import pandas as pd
from app.modules.tasks import TeamManager
from app.schemas.task import StatusUpdate, TeamEdit, createTeam 

router = APIRouter()

team_mgr = TeamManager()


@router.get("/get")
def get_team_details():
    result = team_mgr.get_all_users()
    return result


@router.post("/create-team-details")
def create_team_details(user : createTeam):
    try :
        result = team_mgr.create_team(user)

        return {"message": result["message"]}
        # print("result", df)
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

@router.get("/team")
def get_team_details(team_id: str):
    try :
        result = team_mgr.get_team_by_id(team_id)
        print("result", result)
        return result
    except Exception as e:
        return {"status": "error", "message": str(e)}
    


# @router.put("/team/{team_id}")
# def update_team_details(team_id: str, new_data: createTeam):
#     try :
#         result = team_mgr.update_team(team_id, new_data.dict())
#         # return result
#         return {"message": result["message"], "user": result.get("user")}
    
#     except Exception as e:
#         return {"status": "error", "message": str(e)}
    

@router.put("/edit-team")
def edit_team(payload: TeamEdit):
    try:
        data = team_mgr._read_team()
        if payload.id not in data:
            return {"status": "error", "message": f"Team with id {payload.id} not found"}

        # Update all fields
        data[payload.id] = payload.dict()
        team_mgr._write_teams(data)
        return {"status": "success", "message": "Team updated successfully", "user": data[payload.id]}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    


@router.put("/update-status")
def update_status(payload :StatusUpdate):
    try :
        result = team_mgr.update_status(payload.id,payload.status)
        print("result", result)
    except Exception as e :
        return {"status": "error", "message": str(e)}
    

@router.delete("/delete-details")
def delete_details(team_id :str):
    try :
        result = team_mgr.delete_team(team_id)
        print("result", result)
    except Exception as e :
        return {"status": "error", "message": str(e)}