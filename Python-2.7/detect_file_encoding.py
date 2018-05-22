from chardet.universaldetector import UniversalDetector

with open('/opt/sightmachine/data/folder1/station38_NoBOM.csv', 'r') as f:
    detector = UniversalDetector()
    for line in f.readlines():
        detector.feed(line)
        if detector.done: break
    detector.close()
    f.close()
    print detector.result
