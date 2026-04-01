extends Node2D


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	
	if Input.is_action_just_pressed("w"):
		var t = create_tween()
		t.set_trans(Tween.TRANS_SPRING)
		t.tween_property($Icon/Camera2D, "zoom", Vector2(1.5, 1.5), 2)
		
	if Input.is_action_just_pressed("s"):
		var t = create_tween()
		t.set_trans(Tween.TRANS_SPRING)
		t.tween_property($Icon/Camera2D, "zoom", Vector2(0.5, 0.5), 2)
