import cv2

from utils import read_video,save_video
from trackers import Tracker
from teams_assigner import TeamAssigner

def main():
    #read video
    frames=read_video("input_video/08fd33_4.mp4")





    tracker=Tracker("models/best.pt")



    tracks=tracker.get_object_track(frames,
                                    read_from_stub=True,
                                    stub_path="stubs/tracks_tracks.pkl")



    """for track_id,player in tracks['players'][0].items():
        bbox=player['bbox']
        frame=frames[0]

        cropped_image=frame[int(bbox[1]):int(bbox[3]),int(bbox[0]):int(bbox[2])]
        cv2.imwrite("output_video/cropped_image.jpg",cropped_image)
        break"""

    teams_assigner=TeamAssigner()

    teams_assigner.assign_team_color(frames[0], tracks['players'][0])


    for frame_nb,player_track in enumerate(tracks['players']):
        for player_id ,track in player_track.items():
                team=teams_assigner.get_player_team(
                    frames[frame_nb],
                    track['bbox'],
                    player_id
                )
                tracks['players'][frame_nb][player_id]['teams']=team
                tracks['players'][frame_nb][player_id]['team_color'] = teams_assigner.team_colors[team]






    output_video_frames=tracker.draw_annotations(frames,tracks)

    save_video(output_video_frames, "output_video/output_video.avi")
if __name__=='__main__':
    main()