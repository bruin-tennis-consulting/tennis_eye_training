from ursina import *
import random
import math

app = Ursina()

# =============================================================================
# Tennis Court Dimensions (in meters)
# =============================================================================
# (Assuming 1 unit = 1 meter)

# Court Length: 23.77 m total. Each half is 11.885 m.
COURT_LENGTH = 23.77  
HALF_LENGTH = COURT_LENGTH / 2  # 11.885 m

# Court Width: Singles = 8.23 m, Doubles = 10.97 m.
DOUBLES_WIDTH = 10.97   
HALF_DOUBLES = DOUBLES_WIDTH / 2  # ≈5.485 m
SINGLES_WIDTH = 8.23     
HALF_SINGLES = SINGLES_WIDTH / 2  # ≈4.115 m

# Service line: 6.40 m from the net.
SERVICE_LINE_DISTANCE = 6.40  
# Baselines (ends of the court):
OPPONENT_BASELINE_Z = HALF_LENGTH   # +11.885 m
PLAYER_BASELINE_Z = -HALF_LENGTH    # -11.885 m

# Service lines (parallel to net)
OPPONENT_SERVICE_LINE_Z = SERVICE_LINE_DISTANCE   # +6.40 m
PLAYER_SERVICE_LINE_Z = -SERVICE_LINE_DISTANCE     # -6.40 m

# Net Posts: Distance between posts is 12.80 m (posts at ±6.40 m).
NET_POST_X = 6.40  
NET_HEIGHT_CENTER = 0.91  # Net height at center
NET_HEIGHT_POST = 1.07    # Height at the posts

# =============================================================================
# Fixed Camera Setup (Modified)
# =============================================================================
# Fixed behind the player (no motion or rotation changes).
# Moved farther back (from z=-15 to z=-20). To move even further back, decrease z further.
camera.position = (0, 2.5, -16)
camera.rotation = (5, 0, 0)
camera.fov = 100


# =============================================================================
# Scene Setup: Ground, Net, Court Lines, and Net Posts
# =============================================================================

# Ground: Represents the doubles court.
ground = Entity(
    model='plane',
    scale=(DOUBLES_WIDTH, 1, COURT_LENGTH),
    # Set ground color to #336699:
    color=color.hex('#336699'),
    collider='box'
)
ground.y = 0
# =============================================================================
# Net Setup (Modified)
# =============================================================================
# Create a net grid using a plane with a grid texture.
net = Entity(
    model='plane',
    scale=(12.8, NET_HEIGHT_CENTER, 0.2),  # Spanning between net posts.
    # texture=load_texture('net_grid2.png'),    # Use a valid PNG file.
    position=(0, NET_HEIGHT_CENTER / 2, 0),
    # texture_scale=(4,1)  # Adjust as needed to tile/stretch the texture.
)
# Create a net tape on top of the grid to simulate a thicker top edge.
net_tape = Entity(
    model='cube',
    scale=(12.8, 0.1, 0.21),  # Slightly thicker and extended to cover the top.
    color=color.white,
    position=(0, NET_HEIGHT_CENTER - 0.05, 0)
)



# Net Posts: Positioned at x = ±NET_POST_X, z = 0.
net_post_scale = (0.2, NET_HEIGHT_POST, 0.2)
net_post_y = NET_HEIGHT_POST / 2
net_post_left = Entity(
    model='cube',
    color=color.white,
    scale=net_post_scale,
    position=(-NET_POST_X, net_post_y, 0)
)
net_post_right = Entity(
    model='cube',
    color=color.white,
    scale=net_post_scale,
    position=(NET_POST_X, net_post_y, 0)
)

# --- Court Lines ---
# Use a small thickness and a slight elevation to avoid z-fighting.
line_thickness = 0.05
line_height = 0.05

# Doubles Sidelines (outer boundaries):
left_doubles_sideline = Entity(
    model='cube',
    color=color.white,
    scale=(line_thickness, line_height, COURT_LENGTH),
    position=(-HALF_DOUBLES, line_height/2 + 0.001, 0)
)
right_doubles_sideline = Entity(
    model='cube',
    color=color.white,
    scale=(line_thickness, line_height, COURT_LENGTH),
    position=(HALF_DOUBLES, line_height/2 + 0.001, 0)
)

# Singles Sidelines (inner boundaries):
left_singles_sideline = Entity(
    model='cube',
    color=color.white,
    scale=(line_thickness, line_height, COURT_LENGTH),
    position=(-HALF_SINGLES, line_height/2 + 0.002, 0)
)
right_singles_sideline = Entity(
    model='cube',
    color=color.white,
    scale=(line_thickness, line_height, COURT_LENGTH),
    position=(HALF_SINGLES, line_height/2 + 0.002, 0)
)

# Baselines:
opponent_baseline = Entity(
    model='cube',
    color=color.white,
    scale=(DOUBLES_WIDTH, line_height, line_thickness),
    position=(0, line_height/2 + 0.003, OPPONENT_BASELINE_Z)
)
player_baseline = Entity(
    model='cube',
    color=color.white,
    scale=(DOUBLES_WIDTH, line_height, line_thickness),
    position=(0, line_height/2 + 0.003, PLAYER_BASELINE_Z)
)

# Service Lines (drawn on the singles court):
opponent_service_line = Entity(
    model='cube',
    color=color.white,
    scale=(SINGLES_WIDTH, line_height, line_thickness),
    position=(0, line_height/2 + 0.004, OPPONENT_SERVICE_LINE_Z)
)
player_service_line = Entity(
    model='cube',
    color=color.white,
    scale=(SINGLES_WIDTH, line_height, line_thickness),
    position=(0, line_height/2 + 0.004, PLAYER_SERVICE_LINE_Z)
)

# Center Service Lines: Divide each service box.
opponent_center_service_line = Entity(
    model='cube',
    color=color.white,
    scale=(line_thickness, line_height, SERVICE_LINE_DISTANCE),
    position=(0, line_height/2 + 0.005, OPPONENT_SERVICE_LINE_Z/2)
)
player_center_service_line = Entity(
    model='cube',
    color=color.white,
    scale=(line_thickness, line_height, SERVICE_LINE_DISTANCE),
    position=(0, line_height/2 + 0.005, PLAYER_SERVICE_LINE_Z/2)
)

# Center Marks on Baselines:
center_mark_length = 0.2
opponent_center_mark = Entity(
    model='cube',
    color=color.white,
    scale=(center_mark_length, line_height, line_thickness),
    position=(0, line_height/2 + 0.006, OPPONENT_BASELINE_Z)
)
player_center_mark = Entity(
    model='cube',
    color=color.white,
    scale=(center_mark_length, line_height, line_thickness),
    position=(0, line_height/2 + 0.006, PLAYER_BASELINE_Z)
)


# =============================================================================
# Tennis Ball Setup & Spin (Modified)
# =============================================================================
ball = Entity(
    model='sphere',
    color=color.white,  # Base color changed to white for the seam texture to show clearly.
    scale=0.4,
    position=Vec3(0, 1.5, 10)
)
# Assign a texture with seam lines (ensure the file exists in your assets folder).
ball.texture = load_texture('tennis_ball_seams.png')
SPIN_RATE = 1000  # Degrees per second.


# --- Add (or modify) this new parameter at the top of your code (with your other globals):
BOUNCE_DURATION = 0.25 # Shorter bounce duration (in seconds); default was 0.2



# =============================================================================
# Bounce Zones & Physics Parameters
# =============================================================================
# These zones define where the ball is allowed to land ("in") within the singles court.
# Adjust these values to control how far from the net or baseline the ball bounces.

# For the player's side (near the camera):
PLAYER_BOUNCE_X_MIN = -HALF_SINGLES   # -4.115 m
PLAYER_BOUNCE_X_MAX = HALF_SINGLES    # 4.115 m
# Bounce must be between the service line and just inside the baseline.
PLAYER_BOUNCE_Z_MIN = PLAYER_SERVICE_LINE_Z       # -6.40 m
PLAYER_BOUNCE_Z_MAX = PLAYER_BASELINE_Z + 1.5      # a bit inside the baseline

# For the opponent's side:
OPPONENT_BOUNCE_X_MIN = -HALF_SINGLES  # -4.115 m
OPPONENT_BOUNCE_X_MAX = HALF_SINGLES   # 4.115 m
OPPONENT_BOUNCE_Z_MIN = OPPONENT_SERVICE_LINE_Z     # 6.40 m
OPPONENT_BOUNCE_Z_MAX = OPPONENT_BASELINE_Z - 0.5     # a bit inside the baseline

def random_bounce_position(target_side):
    """Return a random bounce position (with y=0) within the allowed zone for the given side."""
    if target_side == 'player':
        x = random.uniform(PLAYER_BOUNCE_X_MIN, PLAYER_BOUNCE_X_MAX)
        z = random.uniform(PLAYER_BOUNCE_Z_MIN, PLAYER_BOUNCE_Z_MAX)
    else:
        x = random.uniform(OPPONENT_BOUNCE_X_MIN, OPPONENT_BOUNCE_X_MAX)
        z = random.uniform(OPPONENT_BOUNCE_Z_MIN, OPPONENT_BOUNCE_Z_MAX)
    return Vec3(x, 0, z)

# Flight time for a shot (from hit at waist to bounce)
MIN_FLIGHT_TIME = .7
MAX_FLIGHT_TIME = 2

# Bounce parameters:
WAIST_HEIGHT = 2         # Target hit height (approximate waist height)
g = -9.81                # Gravity constant

def compute_initial_velocity(start, bounce, T):
    """
    Compute the initial velocity vector required for the ball to travel from 'start' to 'bounce'
    in time T under gravity. Assumes bounce.y == 0.
    """
    vx = (bounce.x - start.x) / T
    vz = (bounce.z - start.z) / T
    vy = (0 - start.y - 0.5 * g * T * T) / T
    return Vec3(vx, vy, vz)


# =============================================================================
# Rally State Variables
# =============================================================================
# We use a state machine:
# 'flight'  : The ball follows a projectile path from the hit (waist height) to ground contact.
# 'bounce'  : Upon hitting the ground, the ball bounces—retaining its horizontal momentum while
#             receiving an upward impulse—forming a parabolic rebound.
state = 'flight'
current_target_side = 'player'
current_start = ball.position
target_bounce = random_bounce_position(current_target_side)
flight_time = random.uniform(MIN_FLIGHT_TIME, MAX_FLIGHT_TIME)
velocity = compute_initial_velocity(current_start, target_bounce, flight_time)

# =============================================================================
# Main Update Loop: State Machine, Bounce with Forward Momentum, & Ball Spin
# =============================================================================
def update():
    global velocity, state, current_start, target_bounce, flight_time, current_target_side

    dt = time.dt



    # Spin Calculation
    if velocity.z > 0:
        ball.rotation_x += SPIN_RATE * dt
    elif velocity.z < 0:
        ball.rotation_x -= SPIN_RATE * dt



    if state == 'flight':
        # The ball follows its initial projectile flight.
        ball.position += velocity * dt
        velocity.y += g * dt

        # Check for ground contact.
        # In the bounce state (replace the current bounce-up velocity calculation):
        if ball.position.y <= 0:
            ball.position = Vec3(ball.position.x, 0, ball.position.z)
            state = 'bounce'
            # Compute upward velocity so that the ball reaches WAIST_HEIGHT in BOUNCE_DURATION seconds.
            bounce_up_velocity = (WAIST_HEIGHT - 0 - 0.5 * g * (BOUNCE_DURATION**2)) / BOUNCE_DURATION
            velocity = Vec3(velocity.x, bounce_up_velocity, velocity.z)


    elif state == 'bounce':
        # The ball follows a parabolic rebound, retaining forward momentum.
        ball.position += velocity * dt
        velocity.y += g * dt
        # When the ball reaches or exceeds WAIST_HEIGHT, simulate the hit,
        # then compute a new shot (changing target side).
        if ball.position.y >= WAIST_HEIGHT:
            # Spawn a contact marker at the moment the ball reaches waist height.
            ball.position = Vec3(ball.position.x, WAIST_HEIGHT, ball.position.z)
            state = 'flight'
            # Toggle target side for the next shot.
            current_target_side = 'opponent' if current_target_side == 'player' else 'player'
            current_start = ball.position
            target_bounce = random_bounce_position(current_target_side)
            flight_time = random.uniform(MIN_FLIGHT_TIME, MAX_FLIGHT_TIME)
            velocity = compute_initial_velocity(current_start, target_bounce, flight_time)

app.run()
