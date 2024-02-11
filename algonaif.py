import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# calcule la distance euclidienne entre deux points A et B du plan
def distance (A,B):
	i = pow(A[0] - B[0], 2) + pow(A[1] - B[1], 2)
	return math.sqrt(i)

# afficher espace inferieur de W
def afficherPT (l,L,m_l,m_L,PT,r,namefile):
	if (l < L):
		largeur = l
		longueur = L
	else:
		largeur = L
		longueur = l
	figure, axes = plt.subplots()
	for i in range(m_l):
		for j in range(m_L):
			x = PT[i][j][0]
			y = PT[i][j][1]
			drawing = plt.Circle((x,y),r,linestyle='dotted',fill=False)
			axes.add_artist(drawing)		
	axes.set_aspect(1)
	axes.add_patch(Rectangle((0,0),longueur,largeur,fill=False))
	#axes.add_artist(drawing)
	plt.title(f'Surface inférieure de W ({namefile})')
	plt.xlim(0,longueur)
	plt.ylim(0,largeur)
	plt.savefig(f'{namefile}-PT.png')

# renvoie le nombre de positions possibles dans W
def construirePT (l,lambda_l,L,lambda_L,r):
	m_l = int((l - lambda_l) / (2 * r + lambda_l))
	m_L = int((L - lambda_L) / (2 * r + lambda_L))
	PT = []
	for i in range(m_l):
		ligne = []
		for j in range(m_L):
				ligne.append((lambda_L*(j+1)+r*(2*(j+1)-1),lambda_l*(i+1)+r*(2*(i+1)-1)))
		PT.append(ligne)
	return (m_l,m_L,PT)

# instance : ((l,lambda_l),(L,lambda_L),r,arrI,arrF,k)
instances = [((10,0.8),(20,1.0),1,[(0.5,2),(1.3,4),(4,1)],[(2,2),(3,4),(1,3)],2)]

for instance in instances:
	l,lambda_l = instance[0]
	L,lambda_L = instance[1]
	r = instance[2]
	pt = construirePT(l,lambda_l,L,lambda_L,r)
	m_l = pt[0]
	m_L = pt[1]
	PT = pt[2]
	afficherPT(l,L,m_l,m_L,PT,r,f'instance{instances.index(instance)+1}')