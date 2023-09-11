##COMPARACIÓN DE GENES ENTRE Pseudomonas junjuensis y Streptomyces nodosus

#para trabajar con archivos comprimidos
import gzip

# encontrar los genes de Pseudomonas jinjuensis

sequence_file = "uniprotkb_Pseudomonas_jinjuensis.fasta.gz"
set_genes_Pjinjuensis = set()
lista_genes_Pjijuensis = list()

with gzip.open("uniprotkb_Pseudomonas_jinjuensis.fasta.gz", "rt") as file:
    for line in file:
        line = line.rstrip()# seleccion de lineas de titulo
        if line.startswith(">"):
            print(line)

            temp = line.split()
            gene_name = temp[-3]  # extraer nombre del gen
            gene_name = gene_name[3:] #ELIMINO "GN="
            gene_name = gene_name.replace("GN=", "")  # ELIMINO "GN="
            print(temp)
            print(gene_name)
            lista_genes_Pjijuensis.append(gene_name)
            print(lista_genes_Pjijuensis)

            print(len(lista_genes_Pjijuensis)) #contar el numero de genes

            set_genes_Pjinjuensis.add(gene_name) #adicionar los genes al set

#encontrar los genes de Streptomyces nodosus

sequence_file = "uniprotkb_Streptomyces_nodosus.fasta.gz"
set_genes_Snodosus = set()
lista_genes_Snododus = list()

with gzip.open("uniprotkb_Streptomyces_nodosus.fasta.gz", "rt") as file:
    for line in file:
        line = line.rstrip()  # seleccion de lineas de titulo
        if line.startswith(">"):
            print(line)

            temp = line.split()
            gene_name = temp[-3]  # extraer nombre del gen
            gene_name = gene_name[3:]  # ELIMINO "GN="
            gene_name = gene_name.replace("GN=", "")  # ELIMINO "GN="
            print(temp)
            print(gene_name)
            lista_genes_Snododus.append(gene_name)
            print(lista_genes_Snododus)
            print(len(lista_genes_Snododus)) #contar el numero de genes
            set_genes_Snodosus.add(gene_name) #adicionar los genes al set


#encontrar la diferencia de genes entre P. jinjuensis y S. nodosus

    print(set_genes_Pjinjuensis.difference(set_genes_Snodosus))
    print(set_genes_Snodosus.difference(set_genes_Pjinjuensis))
    diferencia = set_genes_Pjinjuensis.difference(set_genes_Snodosus) #genes diferentes entre las bacterias
    print(len(diferencia))
    interseccion = set_genes_Pjinjuensis.intersection(set_genes_Snodosus) #comparten los mismos genes
    print(len(interseccion))