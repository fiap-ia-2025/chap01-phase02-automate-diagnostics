"""
Configuração centralizada para o Sistema de Diagnóstico Automático com NLP
Define todos os paths utilizados pelos notebooks usando paths RELATIVOS
"""

from pathlib import Path
import os

# Detectar automaticamente o diretório raiz do projeto
# Assumindo que este arquivo está em: projeto_root/scripts/config.py
PROJECT_ROOT = Path(__file__).parent.parent.resolve()

# Diretório de documentos (dados e resultados)
DOCUMENTS_DIR = PROJECT_ROOT / 'document'

# Diretório de código-fonte (notebooks)
SRC_DIR = PROJECT_ROOT / 'src'

# ============================================================================
# ARQUIVOS DE ENTRADA (dados brutos)
# ============================================================================
DIAGNOSTICS_CSV = DOCUMENTS_DIR / 'diagnostics.csv'
SYMPTOMS_TXT = DOCUMENTS_DIR / 'symptoms.txt'

# ============================================================================
# ARQUIVOS DE SAÍDA
# ============================================================================
RESULTS_CSV = DOCUMENTS_DIR / 'resultados_diagnostico.csv'
ONTOLOGY_OWL = DOCUMENTS_DIR / 'diagnosticos_ontologia.owl'

# ============================================================================
# Validação: Verificar se diretórios existem
# ============================================================================
def validate_config():
    """Valida se os diretórios e arquivos de entrada existem"""
    errors = []
    
    if not PROJECT_ROOT.exists():
        errors.append(f"❌ Diretório raiz não encontrado: {PROJECT_ROOT}")
    
    if not DOCUMENTS_DIR.exists():
        errors.append(f"❌ Diretório de documentos não encontrado: {DOCUMENTS_DIR}")
    
    if not SRC_DIR.exists():
        errors.append(f"❌ Diretório src não encontrado: {SRC_DIR}")
    
    if not DIAGNOSTICS_CSV.exists():
        errors.append(f"❌ Arquivo não encontrado: {DIAGNOSTICS_CSV}")
    
    if not SYMPTOMS_TXT.exists():
        errors.append(f"❌ Arquivo não encontrado: {SYMPTOMS_TXT}")
    
    if errors:
        print("\n".join(errors))
        raise FileNotFoundError("Falha na validação de configuração")
    
    print("✅ Configuração validada com sucesso!")
    return True


if __name__ == '__main__':
    # Se executado diretamente, valida e exibe a configuração
    validate_config()
    
    print("\n" + "="*70)
    print("CONFIGURAÇÃO DO SISTEMA - PATHS RELATIVOS")
    print("="*70)
    print(f"📁 Raiz do projeto: {PROJECT_ROOT}")
    print(f"📁 Documentos:      {DOCUMENTS_DIR}")
    print(f"📁 Código-fonte:    {SRC_DIR}")
    print(f"\n📥 Entrada (Dados):")
    print(f"   - {DIAGNOSTICS_CSV}")
    print(f"   - {SYMPTOMS_TXT}")
    print(f"\n📤 Saída (Resultados):")
    print(f"   - {RESULTS_CSV}")
    print(f"   - {ONTOLOGY_OWL}")
    print("="*70)
