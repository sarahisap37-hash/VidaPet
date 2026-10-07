from datetime import date

from app.database import Base, engine, SessionLocal
from app import models  # noqa: F401  (registra os modelos no metadata)
from app.crud import inserir_tutor, inserir_animal, inserir_atendimento

Base.metadata.create_all(bind=engine)
print("[OK] Tabelas criadas.")

db = SessionLocal()
hoje = date.today().strftime("%d/%m/%Y")

try:
    t1 = inserir_tutor(db, "Sarah Isabela", "(61) 99999-0001", "sarah.isa@email.com")
    t2 = inserir_tutor(db, "Igor Gabriel", "(61) 99999-0002", "igor.alves@email.com")
    print(f"[OK] Tutores inseridos: {t1.nome_completo} (id={t1.id}), {t2.nome_completo} (id={t2.id})")

    a1 = inserir_animal(db, "Caramelo", "cão", "Vira-lata", 28.5, t1.id)
    a2 = inserir_animal(db, "Pantera", "gato", "Siamês", 4.2, t1.id)
    a3 = inserir_animal(db, "Luna", "ave", "Calopsita", 0.09, t2.id)
    print(f"[OK] Animais inseridos: {a1.nome_animal}, {a2.nome_animal}, {a3.nome_animal}")

    inserir_atendimento(db, hoje, "Vacina anual V8", 120.00, a1.id)
    inserir_atendimento(db, hoje, "Consulta de rotina e vermifugação", 95.00, a2.id)
    inserir_atendimento(db, hoje, "Corte de unhas e avaliação geral", 60.00, a3.id)
    print(f"[OK] 3 atendimentos inseridos na data {hoje}.")
finally:
    db.close()

print("[OK] Sistema VidaPet executado com sucesso.")