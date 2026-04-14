#!/usr/bin/env python3
"""
Script para atualizar triagem_risco.csv com os sintomas atualizado do symptoms.txt
Classifica cada caso como alto ou baixo risco baseado no diagnóstico sugerido
"""

import sys
from pathlib import Path
import pandas as pd

# Adicionar ao path para importar config
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))

from config import DOCUMENTS_DIR, SYMPTOMS_TXT

# Importar o pipeline NLP (será necessário executar o notebook antes)
# Para simplificar, vamos fazer uma classificação baseada em regras

def classify_risk(diagnosis):
    """
    Classifica o risco baseado no diagnóstico
    Alto risco: Infarto, Pneumonia (quando severo), Insuficiência Cardíaca
    Baixo risco: Enxaqueca, Gastrite, Ansiedade
    """
    high_risk_diagnoses = ['Infarto', 'Insuficiência Cardíaca']
    medium_risk_diagnoses = ['Pneumonia']
    
    if diagnosis in high_risk_diagnoses:
        return 'alto risco'
    elif diagnosis in medium_risk_diagnoses:
        return 'alto risco'  # Pneumonia é considerada alto risco
    else:
        return 'baixo risco'


def main():
    # Ler sintomas atualizados
    with open(SYMPTOMS_TXT, 'r', encoding='utf-8') as f:
        symptom_descriptions = [line.strip() for line in f if line.strip()]
    
    print(f"✓ Carregados {len(symptom_descriptions)} sintomas do arquivo atualizado")
    
    # Para agora, vamos usar uma estratégia simplificada:
    # Criar diagnósticos baseados em palavras-chave nos sintomas
    
    diagnoses = []
    for desc in symptom_descriptions:
        desc_lower = desc.lower()
        
        if 'peito' in desc_lower and 'irrad' in desc_lower:
            diagnoses.append('Infarto')
        elif 'peito' in desc_lower and 'aperto' in desc_lower:
            diagnoses.append('Infarto')
        elif 'peito' in desc_lower and 'dor' in desc_lower:
            diagnoses.append('Infarto')
        elif 'tá ficando sem ar' in desc_lower or 'falta de ar' in desc_lower and 'tusso' in desc_lower:
            diagnoses.append('Pneumonia')
        elif 'febre' in desc_lower and 'tusso' in desc_lower and 'respiração' in desc_lower:
            diagnoses.append('Pneumonia')
        elif 'lampejos na vista' in desc_lower or 'zigue-zagues' in desc_lower or 'pulsa' in desc_lower:
            diagnoses.append('Enxaqueca')
        elif 'dor de cabeça' in desc_lower and ('embaçada' in desc_lower or 'nuca' in desc_lower):
            diagnoses.append('Enxaqueca')
        elif 'refluxo' in desc_lower or 'queimação' in desc_lower or 'gastrite' in desc_lower or 'estômago' in desc_lower:
            diagnoses.append('Gastrite')
        elif 'cansado' in desc_lower and 'sem ar' in desc_lower and 'inchado' in desc_lower:
            diagnoses.append('Insuficiência Cardíaca')
        elif 'extremamente cansado' in desc_lower or 'fraqueza' in desc_lower and 'sem ar' in desc_lower:
            diagnoses.append('Insuficiência Cardíaca')
        elif 'ansiedade' in desc_lower or 'nervosismo' in desc_lower or 'palpitações' in desc_lower:
            diagnoses.append('Transtorno de Ansiedade')
        else:
            # Padrão: analisa o contexto
            if 'respiração' in desc_lower or 'catarro' in desc_lower or 'sangue' in desc_lower:
                diagnoses.append('Pneumonia')
            elif 'dor' in desc_lower and 'cabeça' in desc_lower:
                diagnoses.append('Enxaqueca')
            else:
                diagnoses.append('Gastrite')  # Padrão conservador
    
    # Classificar risco
    risks = [classify_risk(diag) for diag in diagnoses]
    
    # Criar DataFrame
    df = pd.DataFrame({
        'sintoma': symptom_descriptions,
        'classificacao': risks
    })
    
    # Salvar
    output_file = DOCUMENTS_DIR / 'triagem_risco.csv'
    df.to_csv(output_file, index=False, encoding='utf-8')
    
    print(f"\n✅ Arquivo atualizado: {output_file}")
    print(f"   Total de casos: {len(df)}")
    print(f"   Alto risco: {(df['classificacao'] == 'alto risco').sum()}")
    print(f"   Baixo risco: {(df['classificacao'] == 'baixo risco').sum()}")
    print(f"\nPrimeiros 5 registros:")
    print(df.head().to_string())


if __name__ == '__main__':
    main()
