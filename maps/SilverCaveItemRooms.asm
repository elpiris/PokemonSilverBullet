	object_const_def
	const SILVERCAVEITEMROOMS_POKE_BALL1
	const SILVERCAVEITEMROOMS_POKE_BALL2
	const SILVERCAVEITEMROOMS_MEWTWO

SilverCaveItemRooms_MapScripts:
	def_scene_scripts

	def_callbacks

SilverCaveItemRoomsMewtwo:
	faceplayer
	opentext
	writetext SilverCaveItemRoomsMewtwoText
	cry MEWTWO
	pause 15
	closetext
	loadvar VAR_BATTLETYPE, BATTLETYPE_FORCEITEM
	loadwildmon MEWTWO, 70
	startbattle
	disappear SILVERCAVEITEMROOMS_MEWTWO
	reloadmapafterbattle
	end

SilverCaveItemRoomsMaxRevive:
	itemball MAX_REVIVE

SilverCaveItemRoomsFullRestore:
	itemball FULL_RESTORE

SilverCaveItemRoomsMewtwoText:
	text "Mew…"
	done

SilverCaveItemRooms_MapEvents:
	db 0, 0 ; filler

	def_warp_events
	warp_event 13,  3, SILVER_CAVE_ROOM_2, 3
	warp_event  7, 15, SILVER_CAVE_ROOM_2, 4

	def_coord_events

	def_bg_events

	def_object_events
	object_event  6,  3, SPRITE_POKE_BALL, SPRITEMOVEDATA_STILL, 0, 0, -1, -1, 0, OBJECTTYPE_ITEMBALL, 0, SilverCaveItemRoomsMaxRevive, EVENT_SILVER_CAVE_ITEM_ROOMS_MAX_REVIVE
	object_event 15, 11, SPRITE_POKE_BALL, SPRITEMOVEDATA_STILL, 0, 0, -1, -1, 0, OBJECTTYPE_ITEMBALL, 0, SilverCaveItemRoomsFullRestore, EVENT_SILVER_CAVE_ITEM_ROOMS_FULL_RESTORE
	object_event 16, 10, SPRITE_MONSTER, SPRITEMOVEDATA_STANDING_DOWN, 0, 0, -1, -1, PAL_NPC_PINK, OBJECTTYPE_SCRIPT, 0, SilverCaveItemRoomsMewtwo, EVENT_SILVER_CAVE_MEWTWO
