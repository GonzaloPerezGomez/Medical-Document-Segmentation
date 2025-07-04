Corpus CodiEsp
/proiektuak/edhia/Corpusak/raw/codiesp

Identificacion de Secciones
/ikerlariak/idelaiglesia004/eriberta/best_models/ClinAIS/public
DESCRIPCIÓN:La tarea se centra en identificar 7 secciones médicas predefinidas en las ECNs (Notas Clínicas Electrónicas), principalmente en las notas de evolución: Enfermedad Actual, Derivación, Antecedentes Personales, Antecedentes Familiares, Exploración, Tratamiento y Evolución.

Modelos a probar:

MODELO: EriBERTa Public - CANTEMIST
SERVIDOR: Mari
RUTA MODELO: /ikerlariak/idelaiglesia004/eriberta/best_models/CANTEMIST/public/best_model
RUTA SALIDA: /ikerlariak/idelaiglesia004/eriberta/results/inference/EriBERTa/CANTEMIST/ann_predictions
ARCHIVO SALIDA: ejemploinforme.ann
DESCRIPCIÓN: Detecta menciones de morfologías tumorales en textos clínicos, clasificadas como MORFOLOGIA_NEOPLASIA.
---------------------------------------------------------------
MODELO: EriBERTa Public - CodiEsp
SERVIDOR: Mari
RUTA MODELO: /ikerlariak/idelaiglesia004/eriberta/best_models/CodiEsp/public/best_model
RUTA SALIDA: /ikerlariak/idelaiglesia004/eriberta/results/inference/EriBERTa/CodiEsp/ann_predictions
ARCHIVO SALIDA: ejemploinforme.ann
DESCRIPCIÓN: Reconoce menciones de diagnósticos y procedimientos clínicos codificables (DIAGNOSTICO, PROCEDIMIENTO).
---------------------------------------------------------------
MODELO: EriBERTa Public - DisTEMIST
SERVIDOR: Mari
RUTA MODELO: /ikerlariak/idelaiglesia004/eriberta/best_models/DisTEMIST/public/best_model
RUTA SALIDA: /ikerlariak/idelaiglesia004/eriberta/results/inference/EriBERTa/DisTEMIST/ann_predictions
ARCHIVO SALIDA: ejemploinforme.ann
DESCRIPCIÓN: Identifica entidades relacionadas con enfermedades mencionadas en los textos clínicos (ENFERMEDAD).
---------------------------------------------------------------
MODELO: EriBERTa Public - MedProcNER
SERVIDOR: Mari
RUTA MODELO: /ikerlariak/idelaiglesia004/eriberta/best_models/MedProcNER/public/best_model
RUTA SALIDA: /ikerlariak/idelaiglesia004/eriberta/results/inference/EriBERTa/MedProcNER/ann_predictions
ARCHIVO SALIDA: ejemploinforme.ann
DESCRIPCIÓN: Detecta procedimientos médicos mencionados en los textos clínicos (PROCEDIMIENTO).
---------------------------------------------------------------
MODELO: EriBERTa Public - MultiCardioNER Track1
SERVIDOR: Mari
RUTA MODELO: /ikerlariak/idelaiglesia004/eriberta/best_models/MultiCardioNER/track1/public/best_model
RUTA SALIDA: /ikerlariak/idelaiglesia004/eriberta/results/inference/EriBERTa/MultiCardioNER/track1/ann_predictions
ARCHIVO SALIDA: ejemploinforme.ann
DESCRIPCIÓN: Identifica enfermedades del ámbito cardiovascular mencionadas en los textos clínicos (ENFERMEDAD).
---------------------------------------------------------------
MODELO: EriBERTa Public - MultiCardioNER Track2
SERVIDOR: Mari
RUTA MODELO: /ikerlariak/idelaiglesia004/eriberta/best_models/MultiCardioNER/track2/public/best_model
RUTA SALIDA: /ikerlariak/idelaiglesia004/eriberta/results/inference/EriBERTa/MultiCardioNER/track2/ann_predictions
ARCHIVO SALIDA: ejemploinforme.ann
DESCRIPCIÓN: Detecta menciones de fármacos utilizados en el contexto de enfermedades cardiovasculares (FARMACO).
---------------------------------------------------------------
MODELO: EriBERTa Public - PharmacoNER Full_Cases
SERVIDOR: Mari
RUTA MODELO: /ikerlariak/idelaiglesia004/eriberta/best_models/PharmacoNER/Full_Cases/public/best_model
RUTA SALIDA: /ikerlariak/idelaiglesia004/eriberta/results/inference/EriBERTa/PharmacoNER/Full_Cases/ann_predictions
ARCHIVO SALIDA: ejemploinforme.ann
DESCRIPCIÓN: Extrae menciones de fármacos (NORMALIZABLES y NO_NORMALIZABLES), proteínas (PROTEINAS) y términos ambiguos (UNCLEAR) en textos clínicos completos.
---------------------------------------------------------------
MODELO: EriBERTa Public - SympTEMIST
SERVIDOR: Mari
RUTA MODELO: /ikerlariak/idelaiglesia004/eriberta/best_models/SympTEMIST/public/best_model
RUTA SALIDA: /ikerlariak/idelaiglesia004/eriberta/results/inference/EriBERTa/SympTEMIST/ann_predictions
ARCHIVO SALIDA: ejemploinforme.ann
DESCRIPCIÓN: Detecta síntomas y signos clínicos presentes en textos médicos (SINTOMA).

MODELO: Modelo para Identificar la Negación
RUTA: /ikerlariak/igoenaga006/EDHIA/SEPIA/models/Negation_Model


