import bpy

outputFile = './Users/nic.motta/Desktop/eje-movimiento/mesh.csv'

verts = [ bpy.context.object.matrix_world @ v.co for v in bpy.context.object.data.vertices ]

csvLines = [ ",".join([ str(v) for v in co ]) + "\n" for co in verts ]

f = open( outputFile, 'w' )
f.writelines( csvLines )
f.close()