from math import sqrt, pow
from fastapi import APIRouter, Depends, HTTPException, status
from schemas import POISchema
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from models import POI

# criando roteador
poi_router = APIRouter(prefix="/poi", tags=["poi"])

# rota para listar todos os pontos de interesse cadastrados
@poi_router.get("/")
async def listar(session: Session = Depends(pegar_sessao)):
    pontos = session.query(POI).all()
    if pontos:
        return pontos
    else:
        return {"mensagem" : "Não há pontos de interesse cadastrados."}

# rota para listar pontos proximos a uma coordenada x y
@poi_router.get("/procurar-proximos")
async def procurar_proximos(x: int, y: int, d_max: int, session: Session = Depends(pegar_sessao)):
    pontos = session.query(POI).all()
    proximos = list()
    for i in pontos:
        x2 = i.x
        y2 = i.y
        dist = sqrt(pow(x - x2, 2) + pow(y - y2, 2)) # distancia entre dois pontos
        if dist <= d_max:
            proximos.append(i)
    if proximos:
        return proximos
    else:
        return {"mensagem" : "Não há pontos de interesse próximos."}
    
# rota para cadastrar ponto de interesse
@poi_router.post("/cadastrar-ponto", status_code=status.HTTP_201_CREATED)
async def cadastrar(poischema: POISchema, session: Session = Depends(pegar_sessao)):
    # filtro: vírgula representa o "AND"
    ponto = session.query(POI).filter(POI.x == poischema.x, POI.y == poischema.y).first()
    
    if ponto:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Já existe um ponto de interesse nessa localização.")
    else:
        novo_ponto = POI(nome=poischema.nome, x=poischema.x, y=poischema.y)
        session.add(novo_ponto)
        session.commit()
        return {"mensagem":f"Ponto {poischema.nome} : ({poischema.x}, {poischema.y}) cadastrado com sucesso."}

@poi_router.delete("/{id_ponto}")
async def apagar_ponto(id_ponto: int, session: Session = Depends(pegar_sessao)):
    ponto = session.query(POI).filter(POI.id == id_ponto).first()

    if not ponto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ponto de interesse não encontrado.")
    else:
        session.delete(ponto)
        session.commit()
        return {"mensagem":f"Ponto {id_ponto} apagado com sucesso."}
