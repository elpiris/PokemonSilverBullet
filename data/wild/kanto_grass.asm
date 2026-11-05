; Kanto Pokémon in grass

KantoGrassWildMons:

	def_grass_wildmons DIGLETTS_CAVE
	db 4 percent, 2 percent, 8 percent ; encounter rates: morn/day/nite
	; morn
	db 17, DIGLETT
	db 19, DIGLETT
	db 21, DIGLETT
	db 15, DIGLETT
	db 21, DUGTRIO
	db 26, DUGTRIO
	db 31, DUGTRIO
	; day
	db 17, DIGLETT
	db 19, DIGLETT
	db 21, DIGLETT
	db 15, DIGLETT
	db 21, DUGTRIO
	db 26, DUGTRIO
	db 31, DUGTRIO
	; nite
	db 17, DIGLETT
	db 19, DIGLETT
	db 21, DIGLETT
	db 15, DIGLETT
	db 21, DUGTRIO
	db 26, DUGTRIO
	db 31, DUGTRIO
	end_grass_wildmons

	def_grass_wildmons MOUNT_MOON
	db 6 percent, 6 percent, 6 percent ; encounter rates: morn/day/nite
	IF DEF(_GOLD)
	; morn
	db 6, ZUBAT
	db 8, GEODUDE
	db 8, SANDSHREW
	db 12, PARAS
	db 10, SANDSLASH
	db 8, CLEFAIRY
	db 8, CLEFAIRY
	; day
	db 6, ZUBAT
	db 8, GEODUDE
	db 8, SANDSHREW
	db 12, PARAS
	db 10, SANDSLASH
	db 8, CLEFAIRY
	db 8, CLEFAIRY
	; nite
	db 6, ZUBAT
	db 8, GEODUDE
	db 8, SANDSHREW
	db 12, PARAS
	db 10, SANDSLASH
	db 8, CLEFAIRY
	db 8, CLEFAIRY
	ELIF DEF(_SILVER)
	; morn
	db 16, ZUBAT
	db 18, GEODUDE
	db 18, ZUBAT
	db 22, PARAS
	db 20, GEODUDE
	db 18, CLEFAIRY
	db 18, CLEFAIRY
	; day
	db 16, ZUBAT
	db 18, GEODUDE
	db 18, ZUBAT
	db 22, PARAS
	db 20, GEODUDE
	db 18, CLEFAIRY
	db 18, CLEFAIRY
	; nite
	db 16, ZUBAT
	db 18, GEODUDE
	db 18, ZUBAT
	db 22, PARAS
	db 20, GEODUDE
	db 18, CLEFAIRY
	db 18, CLEFAIRY
	ENDC
	end_grass_wildmons

	def_grass_wildmons ROCK_TUNNEL_1F
	db 6 percent, 6 percent, 6 percent ; encounter rates: morn/day/nite
	; morn
	db 19, CUBONE
	db 19, GEODUDE
	db 21, MACHOP
	db 17, ZUBAT
	db 23, MACHOKE
	db 22, CUBONE
	db 22, CUBONE
	; day
	db 19, CUBONE
	db 19, GEODUDE
	db 21, MACHOP
	db 17, ZUBAT
	db 23, MACHOKE
	db 22, CUBONE
	db 22, CUBONE
	; nite
	db 19, CUBONE
	db 19, GEODUDE
	db 21, MACHOP
	db 17, ZUBAT
	db 23, MACHOKE
	db 22, CUBONE
	db 22, CUBONE
	end_grass_wildmons

	def_grass_wildmons ROCK_TUNNEL_B1F
	db 6 percent, 6 percent, 6 percent ; encounter rates: morn/day/nite
	; morn
	db 20, CUBONE
	db 20, GEODUDE
	db 24, ONIX
	db 18, ZUBAT
	db 22, MAROWAK
	db 22, KANGASKHAN
	db 22, KANGASKHAN
	; day
	db 20, CUBONE
	db 20, GEODUDE
	db 24, ONIX
	db 18, ZUBAT
	db 22, MAROWAK
	db 22, KANGASKHAN
	db 22, KANGASKHAN
	; nite
	db 20, CUBONE
	db 20, GEODUDE
	db 24, ONIX
	db 18, ZUBAT
	db 22, MAROWAK
	db 22, KANGASKHAN
	db 22, KANGASKHAN
	end_grass_wildmons

	def_grass_wildmons VICTORY_ROAD
	db 6 percent, 6 percent, 6 percent ; encounter rates: morn/day/nite
	IF DEF(_GOLD)
	; morn
	db 32, GRAVELER
	db 32, GOLBAT
	db 33, URSARING
	db 34, ONIX
	db 36, ONIX
	db 35, RHYHORN
	db 35, RHYHORN
	; day
	db 32, GRAVELER
	db 32, GOLBAT
	db 33, URSARING
	db 34, ONIX
	db 36, ONIX
	db 35, RHYHORN
	db 35, RHYHORN
	; nite
	db 32, GRAVELER
	db 32, GOLBAT
	db 33, URSARING
	db 34, ONIX
	db 36, ONIX
	db 35, RHYHORN
	db 35, RHYHORN
	ELIF DEF(_SILVER)
	; morn
	db 32, GRAVELER
	db 32, GOLBAT
	db 33, DONPHAN
	db 34, ONIX
	db 28, LARVITAR
	db 35, RHYHORN
	db 35, RHYHORN
	; day
	db 32, GRAVELER
	db 32, GOLBAT
	db 33, DONPHAN
	db 34, ONIX
	db 28, LARVITAR
	db 35, RHYHORN
	db 35, RHYHORN
	; nite
	db 32, GRAVELER
	db 32, GOLBAT
	db 33, DONPHAN
	db 34, ONIX
	db 28, LARVITAR
	db 35, RHYHORN
	db 35, RHYHORN
	ENDC
	end_grass_wildmons

	def_grass_wildmons TOHJO_FALLS
	IF DEF(_GOLD)
	db 4 percent, 4 percent, 4 percent ; encounter rates: morn/day/nite
	ELIF DEF(_SILVER)
	db 6 percent, 6 percent, 6 percent ; encounter rates: morn/day/nite
	ENDC
	; morn
	db 25, GOLBAT
	db 25, RATICATE
	db 25, GOLBAT
	db 24, SLOWPOKE
	db 23, RATICATE
	db 26, SLOWPOKE
	db 26, SLOWPOKE
	; day
	db 25, GOLBAT
	db 25, RATICATE
	db 25, GOLBAT
	db 24, SLOWPOKE
	db 23, RATICATE
	db 26, SLOWPOKE
	db 26, SLOWPOKE
	; nite
	db 25, GOLBAT
	db 25, RATICATE
	db 25, GOLBAT
	db 24, SLOWPOKE
	db 23, RATICATE
	db 26, SLOWPOKE
	db 26, SLOWPOKE
	end_grass_wildmons

	def_grass_wildmons ROUTE_1
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	; morn
	db 16, PIDGEY
	db 16, RATTATA
	db 17, FURRET
	db 17, PIDGEY
	db 20, FURRET
	db 18, PIDGEOTTO
	db 18, PIDGEOTTO
	; day
	db 16, PIDGEY
	db 16, RATTATA
	db 17, FURRET
	db 17, PIDGEY
	db 20, FURRET
	db 18, PIDGEOTTO
	db 18, PIDGEOTTO
	; nite
	db 16, HOOTHOOT
	db 16, RATTATA
	db 17, RATTATA
	db 17, HOOTHOOT
	db 20, RATICATE
	db 18, HOOTHOOT
	db 18, HOOTHOOT
	end_grass_wildmons

	def_grass_wildmons ROUTE_2
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	IF DEF(_GOLD)
	; morn
	db 3, CATERPIE
	db 3, PIDGEY
	db 5, METAPOD
	db 7, BUTTERFREE
	db 7, PIDGEOTTO
	db 4, PIKACHU
	db 4, PIKACHU
	; day
	db 3, CATERPIE
	db 3, PIDGEY
	db 5, METAPOD
	db 7, PIDGEY
	db 7, PIDGEOTTO
	db 4, PIKACHU
	db 4, PIKACHU
	; nite
	db 3, HOOTHOOT
	db 3, SPINARAK
	db 5, HOOTHOOT
	db 7, NOCTOWL
	db 7, ARIADOS
	db 4, PIKACHU
	db 4, PIKACHU
	ELIF DEF(_SILVER)
	; morn
	db 16, BEEDRILL
	db 16, LEDYBA
	db 18, BEEDRILL
	db 20, BEEDRILL
	db 20, LEDIAN
	db 17, PIKACHU
	db 17, PIKACHU
	; day
	db 16, BEEDRILL
	db 16, PIDGEY
	db 18, BEEDRILL
	db 20, PIDGEOTTO
	db 20, PIDGEOTTO
	db 17, PIKACHU
	db 17, PIKACHU
	; nite
	db 16, HOOTHOOT
	db 16, HOOTHOOT
	db 18, HOOTHOOT
	db 20, NOCTOWL
	db 20, NOCTOWL
	db 17, PIKACHU
	db 17, PIKACHU
	ENDC
	end_grass_wildmons

	def_grass_wildmons ROUTE_3
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	IF DEF(_GOLD)
	; morn
	db 5, SPEAROW
	db 5, RATTATA
	db 8, SPEAROW
	db 6, JIGGLYPUFF
	db 10, RATTATA
	db 8, SPEAROW
	db 8, SPEAROW
	; day
	db 5, SPEAROW
	db 5, RATTATA
	db 8, SPEAROW
	db 6, JIGGLYPUFF
	db 10, RATTATA
	db 8, SPEAROW
	db 8, SPEAROW
	; nite
	db 5, RATTATA
	db 5, ZUBAT
	db 8, RATTATA
	db 6, JIGGLYPUFF
	db 10, RATTATA
	db 8, RATTATA
	db 8, RATTATA
	ELIF DEF(_SILVER)
	; morn
	db 16, SPEAROW
	db 16, RATTATA
	db 19, EKANS
	db 17, JIGGLYPUFF
	db 21, ARBOK
	db 19, SPEAROW
	db 19, SPEAROW
	; day
	db 16, SPEAROW
	db 16, RATTATA
	db 19, EKANS
	db 17, JIGGLYPUFF
	db 21, ARBOK
	db 19, SPEAROW
	db 19, SPEAROW
	; nite
	db 16, RATTATA
	db 16, ZUBAT
	db 19, EKANS
	db 17, JIGGLYPUFF
	db 21, ARBOK
	db 19, RATTATA
	db 19, RATTATA
	ENDC
	end_grass_wildmons

	def_grass_wildmons ROUTE_4
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	; morn
	IF DEF(_GOLD)
	; morn
	db 5, SPEAROW
	db 5, RATTATA
	db 8, SPEAROW
	db 6, JIGGLYPUFF
	db 10, RATTATA
	db 8, SPEAROW
	db 8, SPEAROW
	; day
	db 5, SPEAROW
	db 5, RATTATA
	db 8, SPEAROW
	db 6, JIGGLYPUFF
	db 10, RATTATA
	db 8, SPEAROW
	db 8, SPEAROW
	; nite
	db 5, SPEAROW
	db 5, ZUBAT
	db 8, RATTATA
	db 6, JIGGLYPUFF
	db 10, RATTATA
	db 8, RATTATA
	db 8, RATTATA
	ELIF DEF(_SILVER)
	; morn
	db 17, SPEAROW
	db 17, RATTATA
	db 20, EKANS
	db 18, JIGGLYPUFF
	db 22, ARBOK
	db 20, FEAROW
	db 20, FEAROW
	; day
	db 17, SPEAROW
	db 17, RATTATA
	db 20, EKANS
	db 18, JIGGLYPUFF
	db 22, ARBOK
	db 20, FEAROW
	db 20, FEAROW
	; nite
	db 17, RATTATA
	db 17, ZUBAT
	db 20, EKANS
	db 18, JIGGLYPUFF
	db 22, ARBOK
	db 20, RATICATE
	db 20, RATICATE
	ENDC
	end_grass_wildmons

	def_grass_wildmons ROUTE_5
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	IF DEF(_GOLD)
	; morn
	db 13, PIDGEY
	db 13, BELLSPROUT
	db 14, PIDGEY
	db 15, PIDGEY
	db 12, ABRA
	db 14, ABRA
	db 14, ABRA
	; day
	db 13, PIDGEY
	db 13, BELLSPROUT
	db 14, PIDGEY
	db 15, PIDGEY
	db 12, ABRA
	db 14, ABRA
	db 14, ABRA
	; nite
	db 13, ODDISH
	db 14, ODDISH
	db 13, BELLSPROUT
	db 15, GLOOM
	db 12, ABRA
	db 14, ABRA
	db 14, ABRA
	ELIF DEF(_SILVER)
	; morn
	db 22, PIDGEOTTO
	db 22, WEEPINBELL
	db 23, MEOWTH
	db 24, PIDGEOTTO
	db 21, KADABRA
	db 23, KADABRA
	db 23, KADABRA
	; day
	db 22, PIDGEOTTO
	db 22, WEEPINBELL
	db 23, MEOWTH
	db 24, PIDGEOTTO
	db 21, KADABRA
	db 23, KADABRA
	db 23, KADABRA
	; nite
	db 22, GLOOM
	db 23, MEOWTH
	db 22, WEEPINBELL
	db 24, GLOOM
	db 21, KADABRA
	db 23, KADABRA
	db 23, KADABRA
	ENDC
	end_grass_wildmons

	def_grass_wildmons ROUTE_6
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	IF DEF(_GOLD)
	; morn
	db 13, PIDGEY
	db 13, BELLSPROUT
	db 14, PIDGEY
	db 15, MAGNEMITE
	db 12, ABRA
	db 14, ABRA
	db 14, ABRA
	; day
	db 13, PIDGEY
	db 13, BELLSPROUT
	db 14, PIDGEY
	db 15, MAGNEMITE
	db 12, ABRA
	db 14, ABRA
	db 14, ABRA
	; nite
	db 13, ODDISH
	db 14, ODDISH
	db 13, BELLSPROUT
	db 15, MAGNEMITE
	db 12, ABRA
	db 14, ABRA
	db 14, ABRA
	ELIF DEF(_SILVER)
	; morn
	db 22, PIDGEOTTO
	db 22, WEEPINBELL
	db 23, MEOWTH
	db 24, MAGNEMITE
	db 21, KADABRA
	db 23, KADABRA
	db 23, KADABRA
	; day
	db 22, PIDGEOTTO
	db 22, WEEPINBELL
	db 23, MEOWTH
	db 24, MAGNEMITE
	db 21, KADABRA
	db 23, KADABRA
	db 23, KADABRA
	; nite
	db 22, GLOOM
	db 23, MEOWTH
	db 22, WEEPINBELL
	db 24, MAGNEMITE
	db 21, KADABRA
	db 23, KADABRA
	db 23, KADABRA
	ENDC
	end_grass_wildmons

	def_grass_wildmons ROUTE_7
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	IF DEF(_GOLD)
	; morn
	db 17, RATTATA
	db 17, SPEAROW
	db 18, GROWLITHE
	db 19, RATICATE
	db 19, RATTATA
	db 15, RATTATA
	db 15, RATTATA
	; day
	db 17, RATTATA
	db 17, SPEAROW
	db 18, GROWLITHE
	db 19, RATICATE
	db 19, RATTATA
	db 15, GROWLITHE
	db 15, GROWLITHE
	; nite
	db 17, RATTATA
	db 17, MURKROW
	db 18, GROWLITHE
	db 19, RATICATE
	db 19, MURKROW
	db 15, HOUNDOUR
	db 15, HOUNDOUR
	ELIF DEF(_SILVER)
	; morn
	db 24, MEOWTH
	db 24, FEAROW
	db 25, VULPIX
	db 26, RATICATE
	db 26, PERSIAN
	db 22, RATICATE
	db 22, RATICATE
	; day
	db 24, MEOWTH
	db 24, FEAROW
	db 25, VULPIX
	db 26, RATICATE
	db 26, PERSIAN
	db 22, VULPIX
	db 22, VULPIX
	; nite
	db 24, MEOWTH
	db 24, MURKROW
	db 25, VULPIX
	db 26, RATICATE
	db 26, PERSIAN
	db 22, HOUNDOUR
	db 22, HOUNDOUR
	ENDC
	end_grass_wildmons

	def_grass_wildmons ROUTE_8
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	IF DEF(_GOLD)
	; morn
	db 17, PIDGEOTTO
	db 19, PIDGEOTTO
	db 15, ABRA
	db 18, GROWLITHE
	db 17, PIDGEOTTO
	db 15, KADABRA
	db 15, KADABRA
	; day
	db 17, PIDGEOTTO
	db 19, PIDGEOTTO
	db 15, ABRA
	db 18, GROWLITHE
	db 17, PIDGEOTTO
	db 15, KADABRA
	db 15, KADABRA
	; nite
	db 17, NOCTOWL
	db 20, HAUNTER
	db 15, ABRA
	db 19, NOCTOWL
	db 18, GROWLITHE
	db 15, KADABRA
	db 15, KADABRA
	ELIF DEF(_SILVER)
	; morn
	db 23, MEOWTH
	db 25, PIDGEOTTO
	db 21, KADABRA
	db 24, VULPIX
	db 23, PIDGEOTTO
	db 21, KADABRA
	db 21, KADABRA
	; day
	db 23, MEOWTH
	db 25, PIDGEOTTO
	db 21, KADABRA
	db 24, VULPIX
	db 23, PIDGEOTTO
	db 21, KADABRA
	db 21, KADABRA
	; nite
	db 23, MEOWTH
	db 26, HAUNTER
	db 21, KADABRA
	db 25, NOCTOWL
	db 24, VULPIX
	db 21, KADABRA
	db 21, KADABRA
	ENDC
	end_grass_wildmons

	def_grass_wildmons ROUTE_9
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	IF DEF(_GOLD)
	; morn
	db 13, MANKEY
	db 15, RATTATA
	db 13, SPEAROW
	db 15, RATICATE
	db 15, FEAROW
	db 15, PRIMEAPE
	db 15, PRIMEAPE
	; day
	db 13, MANKEY
	db 15, RATTATA
	db 13, SPEAROW
	db 15, RATICATE
	db 15, FEAROW
	db 15, PRIMEAPE
	db 15, PRIMEAPE
	; nite
	db 13, MANKEY
	db 15, RATTATA
	db 15, RATICATE
	db 13, RATTATA
	db 15, RATICATE
	db 15, PRIMEAPE
	db 15, PRIMEAPE
	ELIF DEF(_SILVER)
	; morn
	db 22, RATICATE
	db 24, FEAROW
	db 22, FEAROW
	db 24, RATICATE
	db 24, FEAROW
	db 24, RATICATE
	db 24, RATICATE
	; day
	db 22, RATICATE
	db 24, FEAROW
	db 22, FEAROW
	db 24, RATICATE
	db 24, FEAROW
	db 24, RATICATE
	db 24, RATICATE
	; nite
	db 22, RATICATE
	db 24, RATICATE
	db 24, RATICATE
	db 22, RATICATE
	db 24, RATICATE
	db 24, RATICATE
	db 24, RATICATE
	ENDC
	end_grass_wildmons

	def_grass_wildmons ROUTE_10_NORTH
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	; morn
	db 23, FEAROW
	db 24, VOLTORB
	db 23, RATICATE
	db 25, FEAROW
	db 23, QUAGSIRE
	db 22, ELECTABUZZ
	db 22, ELECTABUZZ
	; day
	db 23, FEAROW
	db 24, VOLTORB
	db 24, RATICATE
	db 25, FEAROW
	db 22, ELECTABUZZ
	db 24, ELECTABUZZ
	db 24, ELECTABUZZ
	; nite
	db 23, QUAGSIRE
	db 24, VOLTORB
	db 23, RATICATE
	db 24, QUAGSIRE
	db 25, RATICATE
	db 22, ELECTABUZZ
	db 22, ELECTABUZZ
	end_grass_wildmons

	def_grass_wildmons ROUTE_11
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	; morn
	db 23, DROWZEE
	db 24, RATICATE
	db 24, MAGNEMITE
	db 25, DROWZEE
	db 25, HYPNO
	db 25, HYPNO
	db 25, HYPNO
	; day
	db 23, DROWZEE
	db 24, RATICATE
	db 24, MAGNEMITE
	db 25, DROWZEE
	db 25, HYPNO
	db 25, HYPNO
	db 25, HYPNO
	; nite
	db 23, DROWZEE
	db 24, RATICATE
	db 24, MAGNEMITE
	db 25, DROWZEE
	db 25, HYPNO
	db 25, HYPNO
	db 25, HYPNO
	end_grass_wildmons

	def_grass_wildmons ROUTE_13
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	IF DEF(_GOLD)
	; morn
	db 23, NIDORINA
	db 23, NIDORINO
	db 25, PIDGEOTTO
	db 22, HOPPIP
	db 24, HOPPIP
	db 22, QUAGSIRE
	db 25, CHANSEY
	; day
	db 23, NIDORINA
	db 23, NIDORINO
	db 25, PIDGEOTTO
	db 22, HOPPIP
	db 24, HOPPIP
	db 24, HOPPIP
	db 25, CHANSEY
	; nite
	db 23, NIDORINA
	db 23, NIDORINO
	db 25, NOCTOWL
	db 22, QUAGSIRE
	db 24, QUAGSIRE
	db 24, QUAGSIRE
	db 25, CHANSEY
	ELIF DEF(_SILVER)
	; morn
	db 26, NIDORINO
	db 26, NIDORINA
	db 28, PIDGEOTTO
	db 25, SKIPLOOM
	db 27, JUMPLUFF
	db 28, CHANSEY
	db 28, CHANSEY
	; day
	db 26, NIDORINO
	db 26, NIDORINA
	db 28, PIDGEOTTO
	db 25, SKIPLOOM
	db 27, JUMPLUFF
	db 28, CHANSEY
	db 28, CHANSEY
	; nite
	db 26, NIDORINO
	db 26, NIDORINA
	db 28, NOCTOWL
	db 25, QUAGSIRE
	db 27, QUAGSIRE
	db 28, CHANSEY
	db 28, CHANSEY
	ENDC
	end_grass_wildmons

	def_grass_wildmons ROUTE_14
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	IF DEF(_GOLD)
	; morn
	db 23, NIDORINA
	db 23, NIDORINO
	db 25, PIDGEOTTO
	db 24, HOPPIP
	db 26, SKIPLOOM
	db 22, QUAGSIRE
	db 25, CHANSEY
	; day
	db 23, NIDORINA
	db 23, NIDORINO
	db 25, PIDGEOTTO
	db 24, HOPPIP
	db 26, SKIPLOOM
	db 26, SKIPLOOM
	db 25, CHANSEY
	; nite
	db 23, NIDORINA
	db 23, NIDORINO
	db 25, NOCTOWL
	db 22, QUAGSIRE
	db 24, QUAGSIRE
	db 24, QUAGSIRE
	db 25, CHANSEY
	ELIF DEF(_SILVER)
	; morn
	db 27, NIDORINO
	db 27, NIDORINA
	db 29, PIDGEOTTO
	db 28, JUMPLUFF
	db 30, JUMPLUFF
	db 29, CHANSEY
	db 29, CHANSEY
	; day
	db 27, NIDORINO
	db 27, NIDORINA
	db 29, PIDGEOTTO
	db 28, JUMPLUFF
	db 30, JUMPLUFF
	db 29, CHANSEY
	db 29, CHANSEY
	; nite
	db 27, NIDORINO
	db 27, NIDORINA
	db 29, NOCTOWL
	db 26, QUAGSIRE
	db 28, QUAGSIRE
	db 29, CHANSEY
	db 29, CHANSEY
	ENDC
	end_grass_wildmons

	def_grass_wildmons ROUTE_15
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	IF DEF(_GOLD)
	; morn
	db 23, NIDORINA
	db 23, NIDORINO
	db 25, PIDGEOTTO
	db 22, HOPPIP
	db 24, HOPPIP
	db 22, QUAGSIRE
	db 25, CHANSEY
	; day
	db 23, NIDORINA
	db 23, NIDORINO
	db 25, PIDGEOTTO
	db 22, HOPPIP
	db 24, HOPPIP
	db 24, HOPPIP
	db 25, CHANSEY
	; nite
	db 23, NIDORINA
	db 23, NIDORINO
	db 25, NOCTOWL
	db 22, QUAGSIRE
	db 24, QUAGSIRE
	db 24, QUAGSIRE
	db 25, CHANSEY
	ELIF DEF(_SILVER)
	; morn
	db 28, NIDORINO
	db 28, NIDORINA
	db 30, PIDGEOTTO
	db 27, JUMPLUFF
	db 29, JUMPLUFF
	db 30, CHANSEY
	db 30, CHANSEY
	; day
	db 28, NIDORINO
	db 28, NIDORINA
	db 30, PIDGEOTTO
	db 27, JUMPLUFF
	db 29, JUMPLUFF
	db 30, CHANSEY
	db 30, CHANSEY
	; nite
	db 28, NIDORINO
	db 28, NIDORINA
	db 30, NOCTOWL
	db 27, QUAGSIRE
	db 29, QUAGSIRE
	db 30, CHANSEY
	db 30, CHANSEY
	ENDC
	end_grass_wildmons

	def_grass_wildmons ROUTE_16
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	; morn
	db 27, GRIMER
	db 28, FEAROW
	db 29, GRIMER
	db 30, FEAROW
	db 28, SLUGMA
	db 31, MUK
	db 31, MUK
	; day
	db 27, GRIMER
	db 28, FEAROW
	db 29, GRIMER
	db 30, FEAROW
	db 28, SLUGMA
	db 31, MUK
	db 31, MUK
	; nite
	db 27, GRIMER
	db 28, GRIMER
	db 29, GRIMER
	db 29, MURKROW
	db 28, SLUGMA
	db 31, MUK
	db 31, MUK
	end_grass_wildmons

	def_grass_wildmons ROUTE_17
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	; morn
	db 28, FEAROW
	db 27, GRIMER
	db 29, GRIMER
	db 30, FEAROW
	db 29, SLUGMA
	db 32, MUK
	db 32, MUK
	; day
	db 28, FEAROW
	db 27, SLUGMA
	db 29, GRIMER
	db 30, FEAROW
	db 25, SLUGMA
	db 32, MUK
	db 32, MUK
	; nite
	db 28, GRIMER
	db 27, GRIMER
	db 29, GRIMER
	db 30, MUK
	db 29, SLUGMA
	db 32, MUK
	db 32, MUK
	end_grass_wildmons

	def_grass_wildmons ROUTE_18
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	; morn
	db 28, GRIMER
	db 29, FEAROW
	db 30, GRIMER
	db 31, FEAROW
	db 29, SLUGMA
	db 32, MUK
	db 32, MUK
	; day
	db 28, GRIMER
	db 29, FEAROW
	db 30, GRIMER
	db 31, FEAROW
	db 29, SLUGMA
	db 32, MUK
	db 32, MUK
	; nite
	db 28, GRIMER
	db 29, GRIMER
	db 30, GRIMER
	db 30, MUK
	db 29, SLUGMA
	db 32, MUK
	db 32, MUK
	end_grass_wildmons

	def_grass_wildmons ROUTE_21
	db 6 percent, 6 percent, 6 percent ; encounter rates: morn/day/nite
	; morn
	db 30, TANGELA
	db 25, TANGELA
	db 35, TANGELA
	db 20, TANGELA
	db 30, TANGELA
	db 28, MR__MIME
	db 28, MR__MIME
	; day
	db 30, TANGELA
	db 25, TANGELA
	db 35, TANGELA
	db 20, TANGELA
	db 28, MR__MIME
	db 30, MR__MIME
	db 30, MR__MIME
	; nite
	db 30, TANGELA
	db 25, TANGELA
	db 35, TANGELA
	db 20, TANGELA
	db 30, TANGELA
	db 28, MR__MIME
	db 28, MR__MIME
	end_grass_wildmons

	def_grass_wildmons ROUTE_22
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	; morn
	db 16, RATTATA
	db 16, SPEAROW
	db 18, SPEAROW
	db 17, DODUO
	db 19, PONYTA
	db 20, FEAROW
	db 20, FEAROW
	; day
	db 16, RATTATA
	db 16, SPEAROW
	db 18, SPEAROW
	db 17, DODUO
	db 19, PONYTA
	db 20, FEAROW
	db 20, FEAROW
	; nite
	db 16, RATTATA
	db 16, RATTATA
	db 18, RATTATA
	db 17, RATTATA
	db 19, PONYTA
	db 20, RATICATE
	db 20, RATICATE
	end_grass_wildmons

	def_grass_wildmons ROUTE_24
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	; morn
	db 17, BELLSPROUT
	db 19, BELLSPROUT
	db 18, KADABRA
	db 21, WEEPINBELL
	db 17, VENONAT
	db 23, WEEPINBELL
	db 23, WEEPINBELL
	; day
	db 17, BELLSPROUT
	db 19, SUNKERN
	db 18, KADABRA
	db 21, WEEPINBELL
	db 19, BELLSPROUT
	db 23, WEEPINBELL
	db 23, WEEPINBELL
	; nite
	db 17, VENONAT
	db 19, ODDISH
	db 18, KADABRA
	db 22, WEEPINBELL
	db 19, BELLSPROUT
	db 19, VENOMOTH
	db 19, VENOMOTH
	end_grass_wildmons

	def_grass_wildmons ROUTE_25
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	; morn
	db 18, PIDGEOTTO
	db 20, BELLSPROUT
	db 18, VENONAT
	db 19, KADABRA
	db 20, PIDGEOTTO
	db 24, WEEPINBELL
	db 24, WEEPINBELL
	; day
	db 18, PIDGEOTTO
	db 20, BELLSPROUT
	db 20, PIDGEOTTO
	db 19, KADABRA
	db 22, PIDGEOTTO
	db 24, WEEPINBELL
	db 24, WEEPINBELL
	; nite
	db 18, VENONAT
	db 20, ODDISH
	db 20, VENOMOTH
	db 19, KADABRA
	db 24, WEEPINBELL
	db 20, BELLSPROUT
	db 20, BELLSPROUT
	end_grass_wildmons

	def_grass_wildmons ROUTE_26
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	IF DEF(_GOLD)
	; morn
	db 28, DODUO
	db 28, SANDSLASH
	db 32, PONYTA
	db 30, DODUO
	db 30, DODRIO
	db 30, RATICATE
	db 30, QUAGSIRE
	; day
	db 28, DODUO
	db 28, SANDSLASH
	db 32, PONYTA
	db 30, DODUO
	db 30, RATICATE
	db 30, DODRIO
	db 30, DODRIO
	; nite
	db 28, RATICATE
	db 28, SANDSLASH
	db 32, PONYTA
	db 30, RATICATE
	db 30, QUAGSIRE
	db 32, QUAGSIRE
	db 32, QUAGSIRE
	ELIF DEF(_SILVER)
	; morn
	db 28, DODUO
	db 28, RATICATE
	db 32, PONYTA
	db 30, DODUO
	db 30, ARBOK
	db 30, RATICATE
	db 30, QUAGSIRE
	; day
	db 28, DODUO
	db 28, RATICATE
	db 32, PONYTA
	db 30, DODUO
	db 30, RATICATE
	db 30, ARBOK
	db 30, ARBOK
	; nite
	db 28, RATICATE
	db 28, RATICATE
	db 32, PONYTA
	db 30, RATICATE
	db 30, QUAGSIRE
	db 30, ARBOK
	db 30, ARBOK
	ENDC
	end_grass_wildmons

	def_grass_wildmons ROUTE_27
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	IF DEF(_GOLD)
	; morn
	db 28, DODUO
	db 28, RATICATE
	db 30, DODUO
	db 28, QUAGSIRE
	db 32, PONYTA
	db 30, SANDSLASH
	db 30, SANDSLASH
	; day
	db 28, DODUO
	db 28, RATICATE
	db 30, DODUO
	db 30, RATICATE
	db 32, PONYTA
	db 30, SANDSLASH
	db 30, SANDSLASH
	; nite
	db 28, QUAGSIRE
	db 28, RATICATE
	db 30, QUAGSIRE
	db 30, RATICATE
	db 32, PONYTA
	db 30, SANDSLASH
	db 30, SANDSLASH
	ELIF DEF(_SILVER)
	; morn
	db 28, DODUO
	db 28, ARBOK
	db 30, DODUO
	db 28, QUAGSIRE
	db 32, PONYTA
	db 30, DODRIO
	db 30, DODRIO
	; day
	db 28, DODUO
	db 28, ARBOK
	db 30, DODUO
	db 30, RATICATE
	db 32, PONYTA
	db 30, DODRIO
	db 30, DODRIO
	; nite
	db 28, QUAGSIRE
	db 28, ARBOK
	db 30, QUAGSIRE
	db 30, RATICATE
	db 32, PONYTA
	db 32, QUAGSIRE
	db 32, QUAGSIRE
	ENDC
	end_grass_wildmons

	def_grass_wildmons ROUTE_28
	db 10 percent, 10 percent, 10 percent ; encounter rates: morn/day/nite
	IF DEF(_GOLD)
	; morn
	db 39, TANGELA
	db 40, PONYTA
	db 40, URSARING
	db 42, RAPIDASH
	db 41, DODUO
	db 43, DODRIO
	db 43, DODRIO
	; day
	db 39, TANGELA
	db 40, PONYTA
	db 40, URSARING
	db 42, RAPIDASH
	db 41, DODUO
	db 43, DODRIO
	db 43, DODRIO
	; nite
	db 39, TANGELA
	db 40, PONYTA
	db 40, URSARING
	db 40, SNEASEL
	db 42, RAPIDASH
	db 42, RAPIDASH
	db 42, RAPIDASH
	ELIF DEF(_SILVER)
	; morn
	db 39, TANGELA
	db 40, RAPIDASH
	db 40, DONPHAN
	db 42, RAPIDASH
	db 41, DODRIO
	db 43, DODRIO
	db 43, DODRIO
	; day
	db 39, TANGELA
	db 40, RAPIDASH
	db 40, DONPHAN
	db 42, RAPIDASH
	db 41, DODRIO
	db 43, DODRIO
	db 43, DODRIO
	; nite
	db 39, TANGELA
	db 40, RAPIDASH
	db 40, DONPHAN
	db 40, SNEASEL
	db 42, RAPIDASH
	db 42, RAPIDASH
	db 42, RAPIDASH
	ENDC
	end_grass_wildmons

	db -1 ; end
