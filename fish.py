import sys
import pygame,os
from pygame.locals import *
import random

class food():
	def __init__(self,x,y):
		self.x,self.y=x,y
		self.avail=True
		self.regis=[]
	def deliver(self):
			minst=101
			id=len(tank)
			for i in self.regis:
				if(tank[i].st<minst):
					minst=tank[i].st
					id=i
			if(id!=len(tank)):
				tank[id].st=fishAttainHealthafterFood
				tank[id].turn=foodturnfact
				self.avail=False
	def reg(self,j):
		self.regis.append(j)
	def display(self):
		pygame.draw.circle(screen,(0,0,0),(self.x,self.y),foodsize)
						
			
	
class fish():
	def __init__(self,p,s,c,xv,yv):
		self.x=p[0]
		self.y=p[1]
		self.s=s
		self.c=c
		self.xv=xv
		self.yv=yv
		self.st=100
		self.turn=foodturnfact
	def speed(self,j):
		fi=len(foods)
		if(self.st<=fishIgnoreEatHealtabove):
			mind=foodvision+1
			x,y=0,0
			fi=len(foods)
			for i in range(len(foods)):
				d=(((foods[i].x-self.x)**2)+((foods[i].y-self.y)**2))**0.5
				if(d<=foodvision and d<mind):
						mind=d
						x,y=foods[i].x,foods[i].y
						fi=i
			if(mind<=foodvision):
				self.xv+= (x-self.x)*self.turn
				self.yv+= (y-self.y)*self.turn
				self.turn+=addfoodturnfact
			
		self.x+=self.xv
		self.y+=self.yv
		if(self.x>=w-xbound):
			self.xv-=turnfact
		if(self.x<=xbound):
			self.xv+=turnfact
		if(self.y>=h-ybound):
			self.yv-=turnfact
		if(self.y<=ybound):
			self.yv+=turnfact
		
		v=((self.xv**2) + (self.yv**2))**0.5
		if(v>maxvel):
			self.xv=(self.xv/v)*maxvel
			self.yv=(self.yv/v)*maxvel
			v=((self.xv**2) + (self.yv**2))**0.5
		self.st-=MaxVel_StaminaRed*(v/maxvel)
		self.st-=staminaRedForLiving
		
		if(fi!=len(foods)):
			d=(((foods[fi].x-self.x)**2)+((foods[fi].y-self.y)**2))**0.5
			if(d<=self.s+foodsize):
				foods[fi].reg(j)
		else:
			self.turn=foodturnfact
		
	def display(self):
		s=self.s/2.5
		pygame.draw.circle(screen,(0,0,0),(self.x,self.y),self.s)
		pygame.draw.circle(screen,self.c,(self.x,self.y),self.s-3)
		pygame.draw.line(screen,(0,0,0),(self.x,self.y),(self.x+(self.xv*s),self.y+(self.yv*s)),3)
		r=int(255*(1-(self.st/100)))
		pygame.draw.circle(screen,(r,0,0),(self.x,self.y),6)
def r(n,s=0):
	return random.randrange(s,n)
def ro(n):
	for i in range(n):
		obj=fish((r(w-xbound,xbound),r(h-ybound,ybound)),r(15,10),(0,r(256,85),r(256,85)),r(maxvel+1,-maxvel),r(maxvel+1,-maxvel))
		tank.append(obj)
def rfo(n):
	for i in range(n):
		f=food(r(w-xbound-foodvision,xbound+foodvision),r(h-ybound-foodvision,ybound+foodvision))
		foods.append(f)
def fishch(s):
	if(s.st<=0):
		return False
	else:
		return True
def foch(s):
	return s.avail
def tt(txt,s,c,p):
	font = pygame.font.Font('freesansbold.ttf',s)
	text = font.render(txt,True,c)
	textRect = text.get_rect()
	textRect.center = (p[0],p[1])
	screen.blit(text, textRect)

os.environ['SDL_VIDEO_CENTERED'] = '1' 
pygame.init()
info = pygame.display.Info()
pygame.display.set_caption('fish simulation')
w,h= info.current_w-100,info.current_h-100

xbound,ybound=50,50
turnfact=0.9
foodturnfact=0.05
addfoodturnfact=0.01
foodvision=50
MaxVel_StaminaRed=0.25
staminaRedForLiving=0.001
fishnum=100
foodequilibrium=50
fishIgnoreEatHealtabove=90
fishAttainHealthafterFood=100
maxvel=5
foodsize=5

tank=[]
foods=[]
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
ro(fishnum)
rfo(foodequilibrium)
while True:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	if(len(foods)<foodequilibrium):
		rfo(foodequilibrium-len(foods))
	for i in range(len(tank)):
		tank[i].speed(i)
	for i in foods:
		i.deliver()
	tank=list(filter(fishch,tank))
	foods=list(filter(foch,foods))
	screen.fill((200,200,200))
	for i in foods:
		i.display()
	for i in tank:
		i.display()
	tt(f"Fishes : {len(tank)} Food : {len(foods)}",20,(0,0,0),(w//2,h-200))
	pygame.display.update()
