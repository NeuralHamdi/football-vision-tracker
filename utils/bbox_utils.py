def get_center_of_box(bbox):
    return (
        (bbox[0] + bbox[2]) / 2,
        (bbox[1] + bbox[3]) / 2,
    )
def get_bbox_width(bbox):
    return bbox[2] - bbox[0]