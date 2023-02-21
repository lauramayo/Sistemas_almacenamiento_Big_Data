# -*- coding: utf-8 -*-

from datetime import date
from cassandra.cluster import Cluster

############ CLASES #############################################

#CLASES PARA LAS ENTIDADES

class Productor:
    def __init__ (self, CodPro, Productor_Nombre, Pais, OrigenEnergia, MediaProduccion, MaximaProduccion):
        self.CodPro=CodPro
        self.Productor_Nombre=Productor_Nombre
        self.Pais=Pais
        self.OrigenEnergia=OrigenEnergia
        self.MediaProduccion=MediaProduccion
        self.MaximaProduccion=MaximaProduccion
               
class Estacion:
    def __init__ (self, CodEst, Estacion_Nombre):
        self.CodEst=CodEst
        self.Estacion_Nombre=Estacion_Nombre
        
class DistribucionDeRed:
     def __init__ (self, CodDis, LongitudMaxima):
        self.CodDis=CodDis
        self.LongitudMaxima=LongitudMaxima
            
class Linea:
    def __init__ (self, CodLin, Longitud):
        self.CodLin=CodLin
        self.Longitud=Longitud
           
class Subestacion:
    def __init__ (self, CodSub, Capacidad):
        self.CodSub=CodSub
        self.Capacidad=Capacidad
  
class Zona:
    def __init__ (self, ZonCod, Zona_Nombre, Municipios):
        self.ZonCod=ZonCod
        self.Zona_Nombre=Zona_Nombre
        self.Municipios=Municipios
           
class Provincia:
    def __init__ (self, ProCod, JefesProvinciales, Provincia_Nombre):
        self.ProCod=ProCod
        self.JefesProvinciales=JefesProvinciales
        self.Provincia_Nombre=Provincia_Nombre

#CLASES PARA LAS RELACIONES n:m
        
class Provee:
    def __init__ (self, CodPro, CodEst, Provee_Fecha, Provee_Cantidad):
        self.CodPro=CodPro
        self.CodEst=CodEst
        self.Provee_Fecha=Provee_Fecha
        self.Provee_Cantidad=Provee_Cantidad
        
class Distribuye:
    def __init__ (self, CodSub, ZonCod, Distribuye_Fecha, Distribuye_Cantidad):
        self.CodSub=CodSub
        self.ZonCod=ZonCod
        self.Distribuye_Fecha=Distribuye_Fecha
        self.Distribuye_Cantidad=Distribuye_Cantidad


##################### TABLAS SOPORTE #########################################

#He creado una tabla soporte por cada entidad, menos para Linea, pues no es necesaria.
        
#Productor_por_CodPro
#Estacion_por_CodEst       
#DistribucionDeRed_por_CodDis
#Subestacion_por_CodSub
#Zona_por_ZonCod
#Provincia_por_ProCod
        
#FUNCION PARA EXTRAER LOS DATOS DEL PRODUCTOR A PARTIR DEL ID
def extraerDatosProductor (CodPro):
    select = session.prepare ('SELECT * FROM "Productor_por_CodPro" WHERE "Productor_CodPro" = ?') 
    filas= session.execute (select, [CodPro,])
    #Aunque haya solo un productor, Cassandra devuelve un set, por lo que hay que iterar
    for fila in filas:
        p = Productor(CodPro,fila.Productor_Nombre, fila.Productor_Pais, fila.Productor_OrigenEnergia, fila.Productor_MediaProduccion, fila.Productor_MaximaProduccion)
        return p

#FUNCION PARA EXTRAER EL NOMBRE DE LA ESTACION A PARTIR DEL ID 
def extraerDatosEstacion (CodEst):
    select = session.prepare ('SELECT "Estacion_Nombre" FROM "Estacion_por_CodEst" WHERE "Estacion_CodEst" = ?') 
    filas= session.execute (select, [CodEst,])
    #Aunque haya solo una subestacion, Cassandra devuelve un set, por lo que hay que iterar
    for fila in filas:
        est = Estacion (CodEst, fila.Estacion_Nombre) 
        return est

#FUNCION PARA EXTRAER LA LONGITUD MAXIMA DE LA DISTRIBUCION DE RED A PARTIR DEL ID 
def extraerDatosDistribucion (CodDis):
    select = session.prepare ('SELECT "DistribucionDeRed_LongitudMaxima" FROM "DistribucionDeRed_por_CodDis" WHERE "DistribucionDeRed_CodDis" = ?') 
    filas= session.execute (select, [CodDis,])
    #Aunque haya solo una distribucion, Cassandra devuelve un set, por lo que hay que iterar
    for fila in filas:
            dist = DistribucionDeRed (CodDis, fila.DistribucionDeRed_LongitudMaxima) 
            return dist
    
           
#FUNCION PARA EXTRAER LA CAPACIDAD DE LA SUBESTACION A PARTIR DEL ID 
def extraerDatosSubestacion (CodSub):
    select = session.prepare ('SELECT "Subestacion_Capacidad" FROM "Subestacion_por_CodSub" WHERE "Subestacion_CodSub" = ?') 
    filas= session.execute (select, [CodSub,])
    #Aunque haya solo una subestacion, Cassandra devuelve un set, por lo que hay que iterar
    for fila in filas:
        sub = Subestacion (CodSub, fila.Subestacion_Capacidad) 
        return sub
    

#FUNCION PARA EXTRAER LOS DATOS DE LA ZONA A PARTIR DEL ID 
def extraerDatosZona (ZonCod):
    select = session.prepare ('SELECT * FROM "Zona_por_ZonCod" WHERE "Zona_ZonCod" = ?') 
    filas= session.execute (select, [ZonCod,])
    #Aunque haya solo una zona, Cassandra devuelve un set, por lo que hay que iterar
    for fila in filas: 
        zon = Zona (ZonCod,fila.Zona_Nombre, fila.Zona_Municipios) 
        return zon

   
#FUNCION PARA EXTRAER LOS DATOS DE PROVINCIA A PARTIR DEL ID:
#No se usa en los demas apartados, pero se pide.
def extraerDatosProvincia (ProCod):
    select = session.prepare ('SELECT "Provincia_JefesProvinciales", "Provincia_Nombre" FROM "Provincia_por_ProCod" WHERE "Provincia_ProCod" = ?') 
    filas= session.execute (select, [ProCod,])
    #Aunque haya solo una provincia, Cassandra devuelve un set, por lo que hay que iterar
    for fila in filas: 
        pro = Provincia(ProCod, fila.Provincia_JefesProvinciales, fila.Provincia_Nombre)
        return pro


################################## INSERCIONES ###########################

#FUNCION PARA INSERTAR INSTANCIAS DE PRODUCTOR EN LAS TABLAS 1 Y 8
def insertProductor ():
    #Pedimos al usuario los datos del productor
    CodPro= input ("Inserte el id del productor:")
    Productor_Nombre=input ("Inserte el nombre del productor:")
    Pais=input("Inserte el pais de mayor produccion del productor:")
    OrigenEnergia=input("Inserte el origen energetico del productor:")
    MediaProduccion = float (input ("Inserte la produccion media del productor:"))
    MaximaProduccion = float (input ("Inserte la produccion maxima del productor:"))
    p = Productor (CodPro,Productor_Nombre, Pais, OrigenEnergia, MediaProduccion, MaximaProduccion)
    insertProd1 = session.prepare ('INSERT INTO "Tabla1" ("Productor_Pais", "Productor_CodPro", "Productor_MaximaProduccion", "Productor_MediaProduccion", "Productor_Nombre", "Productor_OrigenEnergia") VALUES (?, ?, ?, ?, ?, ?)')
    session.execute (insertProd1, [p.Pais, p.CodPro, p.MaximaProduccion, p.MediaProduccion, p.Productor_Nombre, p.OrigenEnergia])
    insertProd2 = session.prepare('INSERT INTO "Tabla8" ("Productor_Pais", "Productor_OrigenEnergia", "Productor_CodPro", "Productor_MaximaProduccion", "Productor_MediaProduccion", "Productor_Nombre") VALUES (?, ?, ?, ?, ?, ?)')
    session.execute(insertProd2, [p.Pais, p.OrigenEnergia, p.CodPro, p.MaximaProduccion, p.MediaProduccion, p.Productor_Nombre])
    #Insertamos tambien la instancia en la tabla soporte Productor_por_CodPro
    insertProd3 = session.prepare('INSERT INTO "Productor_por_CodPro" ("Productor_CodPro", "Productor_MaximaProduccion", "Productor_MediaProduccion", "Productor_Nombre", "Productor_OrigenEnergia", "Productor_Pais") VALUES (?, ?, ?, ?, ?, ?)')
    session.execute(insertProd3, [p.CodPro, p.MaximaProduccion, p.MediaProduccion, p.Productor_Nombre, p.OrigenEnergia, p.Pais])
    print("Se ha realizado la insercion con exito")

#FUNCION CREADA PARA INSERTAR INSTANCIAS DE ZONA
#No se pide en la actividad
def insertZona ():
    ZonCod=input ("Inserte el id de la zona:")
    Zona_Nombre=input ("Inserte el nombre de la zona:")
    Municipios=set()
    municipio = input ("Introduzca un municipio, vacio para parar")
    while (municipio != ""):
        Municipios.add(municipio)
        municipio = input("Introduzca un municipio, vacio para parar")
    zon=Zona(ZonCod,Zona_Nombre,Municipios)
    insertZona = session.prepare ('INSERT INTO "Zona_por_ZonCod" ("Zona_ZonCod","Zona_Municipios","Zona_Nombre") VALUES (?, ?, ?)')
    session.execute (insertZona, [zon.ZonCod, zon.Municipios, zon.Zona_Nombre])   
    print("Se ha realizado la insercion con exito")


#FUNCION PARA INSERTAR INSTANCIAS DE LA RELACION ENTRE SUBESTACION Y ZONA
def insertDistribuye ():
    #El usuario inserta la cantidad suministrada, y el id de la subestacion y la zona.
    #Los demas datos de la subestacion y la zona se consiguen a traves del id usando las tablas soporte.
    #La fecha se incluye con la funcion date, por simplicidad, pero podria insertarla manualmente el usuario.
    Distribuye_Fecha = date.today()
    Distribuye_Cantidad=float(input("Inserte la cantidad suministrada:"))
    CodSub=input("Inserte el id de la subestacion:")
    ZonCod=input("Inserte el id de la zona:")
    
    sub=extraerDatosSubestacion (CodSub)
    zon=extraerDatosZona (ZonCod)
    if((sub is not None) and (zon is not None)):
        #La insercion se hace en la Tabla5, pues es la que incluye exclusivamente atributos de subestacion y zona.
        insertDist = session.prepare ('INSERT INTO "Tabla5" ("Distribuye_Fecha", "Subestacion_CodSub", "Zona_ZonCod", "Distribuye_Cantidad", "Subestacion_Capacidad", "Zona_Municipios", "Zona_Nombre") VALUES (?, ?, ?, ?, ?, ?, ?)')
        session.execute (insertDist, [Distribuye_Fecha, CodSub, ZonCod, Distribuye_Cantidad, sub.Capacidad, zon.Municipios, zon.Zona_Nombre])
        print("Se ha realizado la insercion con exito")
    #Si no existen a priori datos para esa zona y subestacion en la BD, no se podra insertar la relacion.
    else:
        print("No existen esas instancias de zona y subestacion en la BD")

#FUNCION PARA INSERTAR INSTANCIAS DE LA RELACION ENTRE PRODUCTOR, ESTACION Y DISTRIBUCION DE RED
def insertProvee_Cabecera ():
    #El usuario inserta el id del productor, estacion y distribucion de red.
    #Los demas datos del productor, estacion y distribucion de red se consiguen a traves del id usando las tablas soporte.
    #La fecha y la cantidad de la relacion Provee no fueron consideradas en el modelado, por lo que no deben insertarse.
      
    CodPro=input("Inserte el id del productor:")
    CodEst=input("Inserte el id de la estacion:")
    CodDis=input("Inserte el id de la distribucion de red:")
    
    p=extraerDatosProductor (CodPro)
    est=extraerDatosEstacion (CodEst)
    dis=extraerDatosDistribucion (CodDis)
    if((p is not None) and (est is not None) and (dis is not None)):
        #La insercion se hace en la Tabla7, pues es la que incluye exclusivamente atributos de las tres entidades.
        insertProv_Cab = session.prepare ('INSERT INTO "Tabla7" ("DistribucionDeRed_LongitudMaxima", "DistribucionDeRed_CodDis", "Productor_CodPro", "Estacion_CodEst", "Estacion_Nombre", "Productor_MaximaProduccion", "Productor_MediaProduccion", "Productor_Nombre", "Productor_OrigenEnergia", "Productor_Pais") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
        session.execute (insertProv_Cab, [dis.LongitudMaxima, CodDis, CodPro, CodEst, est.Estacion_Nombre, p.MaximaProduccion, p.MediaProduccion, p.Productor_Nombre, p.OrigenEnergia, p.Pais])
        print("Se ha realizado la insercion con exito")
    #Si no existen a priori datos para ese productor, estacion y distribucion, no se podra insertar la relacion.
    else:
        print("No existen esas instancias de productor, estacion y distribucion en la BD")

    #Actualizamos tambien la Tabla 3 (tipo contador)
    insertContador = session.prepare ('UPDATE \"Tabla3\" SET "Num_DistribucionDeRed" = "Num_DistribucionDeRed" + 1 WHERE "Estacion_CodEst" = ?')
    session.execute(insertContador, [CodEst, ])



######################## ACTUALIZACIONES ###############################
    
#FUNCION PARA ACTUALIZAR EL ORIGEN DE ENERGIA DEL PRODUCTOR EN LA TABLA1
def actualizarOrigenEnergia ():
    #El usuario introduce solo el id del productor y el origen actualizado; el pais (PK de Tabla1) se extrae de la tabla soporte de Productor. 
    CodPro = input ("Inserte id del productor a actualizar:")
    nuevoOrigen = input ("Inserte el nuevo origen de energia:")
    p =extraerDatosProductor (CodPro)
    if (p is not None):
        updateOrigen = session.prepare ('UPDATE "Tabla1" SET "Productor_OrigenEnergia"= ? WHERE "Productor_Pais" = ? AND "Productor_CodPro" = ?')
        session.execute(updateOrigen, [nuevoOrigen, p.Pais, CodPro ])
    else:
        print ("No existe un productor con esa id en la BD")

#FUNCION PARA ACTUALIZAR EL PAIS DEL PRODUCTOR EN LA TABLA1
def actualizarPais ():
    #Como el pais es clave primaria de la tabla, no puede usarse update. Debe hacerse DELETE + INSERT.
    CodPro= input ("Inserte id del productor a actualizar:")
    nuevoPais= input ("Inserte el nuevo pais:")
    p=extraerDatosProductor (CodPro)
    if (p is not None):
        borrar = session.prepare ('DELETE FROM "Tabla1" WHERE "Productor_Pais" = ? AND "Productor_CodPro" = ?')
        session.execute(borrar, [p.Pais, CodPro])
        insert = session.prepare ('INSERT INTO "Tabla1" ("Productor_Pais", "Productor_CodPro", "Productor_MaximaProduccion", "Productor_MediaProduccion", "Productor_Nombre", "Productor_OrigenEnergia") VALUES (?, ?, ?, ?, ?, ?)')
        session.execute (insert, [nuevoPais, CodPro, p.MaximaProduccion, p.MediaProduccion, p.Productor_Nombre, p.OrigenEnergia])
    else:
        print ("No existe un productor con ese id en la BD")



######################### CONSULTAS ####################################
        
#Se llevan a cabo las consultas de la Actividad 1, sobre las tablas creadas para ello.
        
#CONSULTA 1: Obtener los productores buscando por el pais.
#Si existe un productor o mas con ese pais, lo imprimira. De lo contrario, no se imprimira nada.
def consultaProductor_por_Pais ():
    Pais= input ("Inserte el pais buscado:")
    select = session.prepare ('SELECT * FROM "Tabla1" WHERE "Productor_Pais" = ?') 
    productores= session.execute (select, [Pais,])
    for prod in productores:
        p=Productor (prod.Productor_CodPro,prod.Productor_Nombre, Pais, prod.Productor_OrigenEnergia, prod.Productor_MediaProduccion, prod.Productor_MaximaProduccion)
        if (p is not None):
                print ("\n####### id: ", p.CodPro)
                print ("\tNombre: ", p.Productor_Nombre)
                print ("\tPais: ", Pais)
                print ("\tOrigen de energia: ", p.OrigenEnergia)
                print ("\tProduccion maxima: ", p.MaximaProduccion)
                print ("\tProduccion media: ", p.MediaProduccion)
        
#CONSULTA 2: Obtener los jefes provinciales asociados a una zona, buscando por su nombre.
#Si hay una o varias zonas con ese nombre, se imprimiran los jefes provinciales correspondientes
#De lo contrario, no se imprimira nada.
def consultaJefesProvinciales_por_NombreZona ():
    NombreZona= input ("Inserte el nombre de la zona a consultar:")
    select = session.prepare ('SELECT * FROM "Tabla2" WHERE "Zona_Nombre"= ?') 
    filas= session.execute (select, [NombreZona,])
    #Consideramos el caso en que haya mas de una zona con el mismo nombre
    for fila in filas:
        zon= Zona(fila.Zona_ZonCod, NombreZona, fila.Zona_Municipios)
        prov=Provincia(fila.Provincia_ProCod, fila.Provincia_JefesProvinciales, fila.Provincia_Nombre)
        if ((zon is not None)and (prov is not None)):
            #No imprimimos los municipios de la zona, pues no es relevante para la consulta
            print ("\n######## id de la zona: ", zon.ZonCod)
            print ("\tNombre de la zona: ", zon.Zona_Nombre)
            print ("\tid de la provincia: ", prov.ProCod)
            print ("\tJefes provinciales: ")
            for jefe in prov.JefesProvinciales:
                print("\t\t",jefe)
        

#CONSULTA 3: Obtener cuantas distribuciones de red tiene una estacion, de haberlas.
def Num_Distribuciones ():
    CodEst= input ("Inserte el id de la estacion:")
    select = session.prepare ('SELECT "Num_DistribucionDeRed" FROM "Tabla3" WHERE "Estacion_CodEst" = ?') 
    filas= session.execute (select, [CodEst,])
    #Solo hay un dato, pero hay que iterar porque Cassandra devuelve un tipo set
    for fila in filas:
        num=fila.Num_DistribucionDeRed
        if (num is not None):
            print ("La estacion de id ",CodEst,"tiene ",num," distribuciones de red")
        
       
#CONSULTA 4: Consulta la zona en la que se encuentra un municipio en concreto.
def Zona_por_Municipio ():
    #Se pide buscar por un solo municipio, por lo que la PK es de tipo text.
    #Se añade a la Tabla4 otra columna con el conjunto de municipios (tipo set) para mantener el atributo original de Zona.
    municipio=input("Inserte el municipio:")    
    select = session.prepare ('SELECT * FROM "Tabla4" WHERE "Zona_Municipios" = ?') 
    zonas= session.execute (select, [municipio,])
    #Tenemos en cuenta el caso en que haya municipios con el mismo nombre en diferentes zonas.
    for zona in zonas:
        zon=Zona (zona.Zona_ZonCod, zona.Zona_Nombre, zona.Zona_Municipios_set)
        if (zon is not None):
            print("\n######## Nombre de la zona: ",zon.Zona_Nombre)
            print("\tid de la zona: ", zon.ZonCod)
            print("\tMunicipio buscado: ", municipio)
            print("\tMunicipios de la zona: ")
            for mun in zon.Municipios:
                print("\t\t",mun)
            
#CONSULTA 5: Consultar las zonas y subestaciones en las que estas ultimas han suministrado energia, segun una fecha determinada.
def consultaZonas_Subestaciones ():
    #Introducimos la fecha con date por simplicidad, pero podria introducirla manualmente el usuario.
    Fecha=date.today()
    select = session.prepare ('SELECT * FROM "Tabla5" WHERE "Distribuye_Fecha" = ?') 
    filas= session.execute (select, [Fecha,])
    for fila in filas:
        sub=Subestacion (fila.Subestacion_CodSub, fila.Subestacion_Capacidad)
        zon=Zona (fila.Zona_ZonCod, fila.Zona_Nombre, fila.Zona_Municipios)
        if((sub is not None) and (zon is not None)):
            #No imprimimos los municipios de la zona, porque no es relevante para esta consulta.
            print("\n######Fecha: ", Fecha)
            print("\tCantidad suministrada: ", fila.Distribuye_Cantidad)
            print("\tid de la subestacion: ", sub.CodSub)
            print("\tCapacidad de la subestacion: ", sub.Capacidad)
            print("\tid de la zona: ", zon.ZonCod)
            print("\tNombre de la zona: ", zon.Zona_Nombre)
    
       

#CONSULTA 6: Consultar segun el id de una estacion las lineas a las que esta conectada, incluyendo la longitud maxima de la distribucion de red utilizada.
def consultaLineas_Estacion ():
    CodEst=input("Inserte el id de la estacion:")
    select = session.prepare ('SELECT * FROM "Tabla6" WHERE "Estacion_CodEst" = ?') 
    filas= session.execute (select, [CodEst,])
    for fila in filas:
        est=Estacion (CodEst, fila.Estacion_Nombre) 
        dist=DistribucionDeRed (fila.DistribucionDeRed_CodDis, fila.DistribucionDeRed_LongitudMaxima) 
        lin =Linea (fila.Linea_CodLin, fila.Linea_Longitud)
        if ((fila is not None) and (dist is not None) and (lin is not None)):
            print("\n######## id de la estacion: ", CodEst)
            print("Nombre de la estacion: ", est.Estacion_Nombre)
            print("\t########## LINEA:")
            print("\tid de la linea: ", lin.CodLin)
            print("\tLongitud de la linea: ", lin.Longitud)
            print("\tLongitud maxima de la distribucion de red: ", dist.LongitudMaxima)
        


#CONSULTA 7: Obtener los productores que esten asociados a una distribucion de red buscando por su longitud maxima.
def consultaProductores_Distribucion ():
    LongitudMaxima=float(input("Inserte la longitud maxima de la distribucion de red:"))
    select = session.prepare ('SELECT * FROM "Tabla7" WHERE "DistribucionDeRed_LongitudMaxima" = ?') 
    filas= session.execute (select, [LongitudMaxima,])
    for fila in filas:
        est=Estacion (fila.Estacion_CodEst, fila.Estacion_Nombre) 
        dist=DistribucionDeRed (fila.DistribucionDeRed_CodDis, LongitudMaxima) 
        p=Productor (fila.Productor_CodPro,fila.Productor_Nombre, fila.Productor_Pais, fila.Productor_OrigenEnergia, fila.Productor_MediaProduccion, fila.Productor_MaximaProduccion)
        if ((est is not None) and (dist is not None) and (p is not None)):
            print("\n######## Longitud maxima de la distribucion de red: ", LongitudMaxima)
            print("id de la distribucion de red: ", dist.CodDis)
            print("Nombre de la estacion: ",est.Estacion_Nombre)
            print("id de la estacion: ", est.CodEst)
            print ("\t######## PRODUCTOR:")
            print ("\tid: ", p.CodPro)
            print ("\tPais: ", p.Pais)
            print ("\tNombre: ", p.Productor_Nombre)
            print ("\tOrigen de energia: ", p.OrigenEnergia)
            print ("\tProduccion maxima: ", p.MaximaProduccion)
            print ("\tProduccion media: ", p.MediaProduccion)
        

#CONSULTA 8: Obtener los productores buscando por el pais y el origen de energia (composite PK).
def consultaProductor_por_Pais_Origen ():
    #El usuario inserta el pais y el origen energetico
    Pais= input ("Inserte el pais buscado:")
    Origen=input ("Inserte el origen energetico:")
    select = session.prepare ('SELECT * FROM "Tabla8" WHERE "Productor_Pais" = ? AND "Productor_OrigenEnergia" = ?') 
    productores= session.execute (select, [Pais,Origen])
    for prod in productores:
        p=Productor (prod.Productor_CodPro,prod.Productor_Nombre, Pais, Origen, prod.Productor_MediaProduccion, prod.Productor_MaximaProduccion)
        if (p is not None):
            print ("\n####### id: ", p.CodPro)
            print ("\tNombre: ", p.Productor_Nombre)
            print ("\tPais: ", Pais)
            print ("\tOrigen de energia: ", Origen)
            print ("\tProduccion maxima: ", p.MaximaProduccion)
            print ("\tProduccion media: ", p.MediaProduccion)
       
    

################### CONEXION A CASSANDRA ########################   

cluster=Cluster()
session=cluster.connect('lauramolinos')

numero=-1
#Pedimos al usuario la operacion que desea realizar:
while (numero!=0):
    print ("\nIntroduzca un numero para ejecutar una de las siguientes operaciones:")
    print ("\t1. Insertar un nuevo productor")
    print ("\t2. Insertar una relacion entre subestacion y zona")
    print ("\t3. Insertar una relacion entre productor, estacion y distribucion de red")
    print ("\t4. Actualizar el origen de energia del productor (Tabla1)")
    print ("\t5. Actualizar el pais del productor (Tabla1) ")
    print ("\t6. Consultar los datos del productor por pais (consulta 1)")
    print ("\t7. Consultar los datos del productor por pais y origen de energia (consulta 8) ")
    print ("\t8. Consultar los jefes provinciales asociados a una zona (consulta 2)")
    print ("\t9. Consultar cuantas distribuciones de red tiene una estacion (consulta 3)")
    print ("\t10. Consultar la zona en la que se encuentra un municipio en concreto (consulta 4)")
    print ("\t11. Consultar suministros entre subestaciones y zonas, dada una fecha (consulta 5)")
    print ("\t12. Consultar las lineas a las que esta conectada una estacion (consulta 6)")
    print ("\t13. Consultar productores asociados a una distribucion de red (consulta 7)")
    print ("\t0. Cerrar aplicacion")
  
    numero = int (input()) #Pedimos numero al usuario
    if (numero == 1):
        insertProductor ()
    elif (numero == 2):
        insertDistribuye()
    elif (numero == 3):
        insertProvee_Cabecera ()
    elif (numero == 4):
        actualizarOrigenEnergia ()
    elif (numero == 5):
        actualizarPais()
    elif (numero == 6):
        consultaProductor_por_Pais ()
    elif (numero == 7):
        consultaProductor_por_Pais_Origen()
    elif (numero == 8):
        consultaJefesProvinciales_por_NombreZona()
    elif (numero == 9):
        Num_Distribuciones ()
    elif (numero == 10):
        Zona_por_Municipio ()
    elif (numero == 11):
        consultaZonas_Subestaciones ()
    elif (numero == 12):
        consultaLineas_Estacion ()
    elif (numero == 13):
        consultaProductores_Distribucion ()
    
    else:
        print ("Numero no valido")



session.shutdown()


