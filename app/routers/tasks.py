from fastapi import APIRouter
import pandas as pd
from app.modules.tasks import TeamManager
from app.schemas.task import createTeam 

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
        # df = pd.DataFrame([result['message']])
        # return df
        return {"message": result["message"]}
        # print("result", df)
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

@router.get("/team/{team_id}")
def get_team_details(team_id: str):
    try :
        result = team_mgr.get_team_by_id(team_id)
        print("result", result)
        return result
    except Exception as e:
        return {"status": "error", "message": str(e)}
    


@router.put("/team/{team_id}")
def update_team_details(team_id: str, new_data: createTeam):
    try :
        result = team_mgr.update_team(team_id, new_data.dict())
        # return result
        return {"message": result["message"], "user": result.get("user")}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

@router.put("/update-status")
def update_status(team_id :str ,status :str):
    try :
        result = team_mgr.update_status(team_id,status)
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