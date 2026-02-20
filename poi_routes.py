from math import sqrt, pow
from fastapi import APIRouter, Depends, HTTPException
from schemas import POISchema, CoordSchema
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from models import POI

# criando roteador
poi_router = APIRouter(prefix="/poi", tags=["poi"])

# rota para listar todos os pontos de interesse cadastrados
@poi_router.get("/")
async def listar(session: Session = Depends(pegar_sessao)):
    dados = session.query(POI.nome, POI.x, POI.y)
    pontos = {t[0]: (t[1], t[2]) for t in dados}
    if pontos:
        return pontos
    else:
        return {"mensagem" : "Não há pontos de interesse cadastrados."}

# rota para cadastrar ponto de interesse
@poi_router.post("/cadastrar-ponto")
async def cadastrar(poischema: POISchema, session: Session = Depends(pegar_sessao)):
    # filtro: vírgula representa o "AND"
    ponto = session.query(POI).filter(POI.x == poischema.x, POI.y == poischema.y).first()
    
    if ponto:
        raise HTTPException(status_code=400, detail="Já existe um ponto de interesse nessa localização.")
    
    else:
        novo_ponto = POI(nome=poischema.nome, x=poischema.x, y=poischema.y)
        session.add(novo_ponto)
        return {"mensagem":f"Ponto {poischema.nome} : ({poischema.x}, {poischema.y}) cadastrado com sucesso."}


# rota para listar pontos proximos a uma coordenada x y
@poi_router.post("/listar-proximos")
async def listar_proximos(coordschema: CoordSchema, session: Session = Depends(pegar_sessao)):
    dados = session.query(POI.nome, POI.x, POI.y)
    pontos = {t[0] : (t[1], t[2]) for t in dados}
    proximos = dict()
    for i in pontos:
        nome = i
        x = (pontos[i])[0]
        y = (pontos[i])[1]
        dist = sqrt(pow(coordschema.x - x, 2) + pow(coordschema.y - y, 2)) # distancia entre dois pontos
        if dist <= coordschema.d_max:
            proximos[nome] = (x, y)
    if proximos:
        return proximos
    else:
        return {"mensagem" : "Não há pontos de interesse próximos."}