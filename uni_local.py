import os 

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'clear'
    os.system(command)
    
def run():
    
    clearConsole()

    id_correcto = input('id alumno correcto = ')
    id_incorrecto = input('id alumno incorrecto = ')
    id_zendesk = input('id tarjeta = ')

    
    tablas =    ['vader_public.log_trafu_synced', 'creta_respuesta.registros', 'creta_resultado.remediales', 'creta_resultado.resultados_estudiantes', 
                'creta_resultado.resultados_medibles', 'creta_resultado.resultados_practicos_estudiantes', 'edna_public.actividad_remota_estudiante', 
                'kimun_public.registros_scan', 'norma_public.asistencias_acumuladas', 'norma_public.asistencias_mensuales', 'norma_public.avisos_inasistencias', 
                'norma_public.bloque_inasistencias', 'norma_public.bloque_observaciones', 'norma_public.inasistencias', 'norma_public.retiros', 
                'norma_public.sesion_aula_inasistencias', 'norma_public.sesion_aula_observaciones', 'creta_respuesta.aplicacion_online_estudiante', 
                'padawan_public.adjuntos', 'padawan_public.respuestas', 'padawan_public.revision_actividad_remota_estudiante', 'padawan_public.visitas', 
                'public.apoderado_estudiante', 'public.codigos_validaciones_estudiantes', 'public.colisiones_estudiantes', 'public.curso_aula_estudiante', 
                'public.estudiante_seccion', 'public.matriculas', 'public.pre_matriculas', 'public.promociones', 'public.ramo_estudiante', 'saga_public.registros', 
                'sasquatch_public.historial_pie_cursos_estudiantes', 'sasquatch_public.registro_apoyos_estudiantes', 'sasquatch_public.registro_logros_aprendizajes', 
                'vader_public.anotacion_grupal_estudiante', 'vader_public.certificados_accidentes', 'vader_public.fichas_estudiantes', 
                'weisstein_public.bonificaciones_anuales', 'weisstein_public.calificaciones', 'weisstein_public.calificaciones_examenes', 
                'weisstein_public.calificaciones_grupo', 'weisstein_public.detalles_informes', 'weisstein_public.estudiantes_eximidos_cursos', 
                'weisstein_public.estudiantes_graduados', 'weisstein_public.listas_estudiantes_cursos', 'weisstein_public.observaciones_bonificaciones', 
                'weisstein_public.observaciones_estudiantes', 'weisstein_public.promedio_asignatura_anual', 
                'weisstein_public.promedio_asignatura_grupo_calificaciones_periodo', 'weisstein_public.promedio_asignatura_periodo', 
                'weisstein_public.situacion_final_estudiante', 'public.apoderado_estudiante_sync', 'public.pre_matriculas_backup', 
                'odin_public.registro_estudiante_eliminado'
                ]

    tablas2 =   ['public.estudiantes', 'public.matriculas']
    
    tablas3 =   ['edna_public.comentarios', 'edna_public.comentarios_directos' ] 

    select = "Select * from {} where estudiante_id in ('{}', '{}');\n"
    
    select2 = "Select * from {} where id in ('{}', '{}');\n"
    select3 = "Select * from {} where emisor_id in ('{}', '{}');\n"
    
    update = "update {} set estudiante_id = '{}' where estudiante_id = '{}';\n"
    update2 = "update {} set emisor_id = '{}' where emisor_id = '{}';\n"
    
    delete = "delete from {} where id = '{}';\n"
    delete2 = "delete from {} where estudiante_id = '{}';\n"

    docu1 = open('respaldo id_conservar : ' + id_correcto + ' id_a_eliminar ' + id_incorrecto + ' Ticket : ' + id_zendesk + '.sql', 'w')
    docu2 = open('actualizador id_correcto : ' + id_correcto + ' id_a_eliminar ' + id_incorrecto + ' Ticket : ' + id_zendesk + '.sql', 'w')


    for i in tablas:
        
        arch = select.format(i, id_correcto, id_incorrecto)
        arch2 = update.format(i, id_correcto, id_incorrecto)
        docu1.write(arch)
        docu2.write(arch2)
    
    arch5 = select2.format(tablas2[0], id_correcto, id_incorrecto)
  
    docu1.write(arch5)
  
    for i in tablas3:
        
        arch7 = select3.format(i, id_correcto, id_incorrecto)
        arch8 = update2.format(i, id_correcto, id_incorrecto)
        docu1.write(arch7)
        docu2.write(arch8)
        
    docu1.close()        
    
    arch4 = delete.format(tablas2[0], id_incorrecto)  
    arch3 = delete2.format(tablas2[1], id_incorrecto)
    docu2.write(arch4)
    docu2.write(arch3)
    docu2.close()
    print('finalizado')
    
if __name__ == '__main__':
    run()