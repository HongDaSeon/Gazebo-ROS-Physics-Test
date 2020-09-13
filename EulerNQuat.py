def euler_to_quaternion(yaw, pitch, roll):

        qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
        qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
        qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
        qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)

        return [qx, qy, qz, qw]

def quaternion_to_euler(x ,y , z, w):
    sin_r = 2*(w*x + y*z)
    cos_r = -1*(x*x + y*y)
    roll = math.degrees(math.atan2(sin_r, cos_r))

    sin_p = 2*(w*y - z*x)
    if(math.fabs(sin_p) >= 1):
        pitch = math.degrees(math.copysign(math.pi / 2, sin_p))
    else:
        pitch = math.degrees(math.asin(sin_p))
    sin_h = 2*(w*z + x*y)
    cos_h = -1*(y*y + z*z)
    yaw = math.degrees(math.atan2(sin_h, cos_h))

    return yaw, roll, pitch
