#!/usr/bin/python
import os
import subprocess
import sys
import tempfile

args = sys.argv
os.chdir(tempfile.gettempdir())

args.tempfiles = []

if args.isallsensor:
        init_script = """
        ZnJvbSBlbW90aXYgaW1wb3J0IGVwb2MKCmUgPSBlcG9jLkVQT0MoKQoKaGVhZGVyID0gIkdS
        WCBHUlkgRjMgRkM1IEFGMyBGNyBUNyBQNyBPMSBPMiBQOCBUOCBGOCBBRjQgRkM2IEY0IgoK
        ZGVmIGZsb2F0Zm10KHgpOgogICAgICAgIHJldHVybiAiezouMmZ9Ii5mb3JtYXQoeCkKCmYg
        PSBvcGVuKCJlcG9jX2RhdGEiLCJ3IikKZi53cml0ZShoZWFkZXIgKyAiXG4iKQpmLmNsb3Nl
        KCkKCmZvciBpIGluIHhyYW5nZSg1KToKICAgICAgICBzYW1wbGUgPSBlLmdldF9zYW1wbGUo
        KQogICAgICAgIGlmIG5vdCBzYW1wbGUgPT0gW106CiAgICAgICAgICAgICAgICBkYXRhID0g
        W2UuZ3lyb1gsZS5neXJvWV0KICAgICAgICAgICAgICAgIGRhdGEuZXh0ZW5kKHNhbXBsZSkK
        ICAgICAgICAgICAgICAgIGRhdGEgPSAiICIuam9pbihtYXAoZmxvYXRmbXQsZGF0YSkpCiAg
        ICAgICAgICAgICAgICBmID0gb3BlbigiZXBvY19kYXRhIiwiYSIpCiAgICAgICAgICAgICAg
        ICBmLndyaXRlKGRhdGEgKyAiXG4iKQogICAgICAgICAgICAgICAgZi5jbG9zZSgpCgplLmRp
        c2Nvbm5lY3QoKQo=
        """
        tf = tempfile.NamedTemporaryFile(delete=False)
        isname = tf.name
        tf.write(init_script.decode("base64"))
        tf.close()

        os.system("python %s"%tf.name)
        args.tempfiles.append(tf.name)

        read_script = """
        ZnJvbSBlbW90aXYgaW1wb3J0IGVwb2MKCmUgPSBlcG9jLkVQT0MoKQoKZGVmIGZsb2F0Zm10
        KHgpOgogICAgICAgIHJldHVybiAiezouMmZ9Ii5mb3JtYXQoeCkKCndoaWxlIDE6CiAgICAg
        ICAgdHJ5OgogICAgICAgICAgICAgICAgc2FtcGxlID0gZS5nZXRfc2FtcGxlKCkKICAgICAg
        ICAgICAgICAgIGlmIG5vdCBzYW1wbGU9PVtdOgogICAgICAgICAgICAgICAgICAgICAgICBk
        YXRhID0gW2UuZ3lyb1gsZS5neXJvWV0KICAgICAgICAgICAgICAgICAgICAgICAgZGF0YS5l
        eHRlbmQoc2FtcGxlKQogICAgICAgICAgICAgICAgICAgICAgICBkYXRhID0gIiAiLmpvaW4o
        bWFwKGZsb2F0Zm10LGRhdGEpKQogICAgICAgICAgICAgICAgICAgICAgICBmID0gb3Blbigi
        ZXBvY19kYXRhIiwiYSIpCiAgICAgICAgICAgICAgICAgICAgICAgIGYud3JpdGUoZGF0YSAr
        ICJcbiIpCiAgICAgICAgICAgICAgICAgICAgICAgIGYuY2xvc2UoKQogICAgICAgIGV4Y2Vw
        dDoKICAgICAgICAgICAgICAgIGJyZWFrCgplLmRpc2Nvbm5lY3QoKQo=
        """
        tf = tempfile.NamedTemporaryFile(delete=False)
        rsname = tf.name
        tf.write(read_script.decode("base64"))
        tf.close()

        args.tempfiles.append(tf.name)

        plot_script = """
        c2V0IHRlcm1pbmFsIHgxMQpzZXQgbXVsdGlwbG90IGxheW91dCA0LDQKc2V0IGdyaWQKcGxv
        dCAiPCB0YWlsIC0yNTAgZXBvY19kYXRhIiB1c2luZyAxICB3aXRoIHN0ZXBzIHRpdGxlICJH
        UlgiCnBsb3QgIjwgdGFpbCAtMjUwIGVwb2NfZGF0YSIgdXNpbmcgMiAgd2l0aCBzdGVwcyB0
        aXRsZSAiR1JZIgpwbG90ICI8IHRhaWwgLTI1MCBlcG9jX2RhdGEiIHVzaW5nIDMgIHdpdGgg
        c3RlcHMgdGl0bGUgIkYzIgpwbG90ICI8IHRhaWwgLTI1MCBlcG9jX2RhdGEiIHVzaW5nIDQg
        IHdpdGggc3RlcHMgdGl0bGUgIkZDNSIKcGxvdCAiPCB0YWlsIC0yNTAgZXBvY19kYXRhIiB1
        c2luZyA1ICB3aXRoIHN0ZXBzIHRpdGxlICJBRjMiCnBsb3QgIjwgdGFpbCAtMjUwIGVwb2Nf
        ZGF0YSIgdXNpbmcgNiAgd2l0aCBzdGVwcyB0aXRsZSAiRjciCnBsb3QgIjwgdGFpbCAtMjUw
        IGVwb2NfZGF0YSIgdXNpbmcgNyAgd2l0aCBzdGVwcyB0aXRsZSAiVDciCnBsb3QgIjwgdGFp
        bCAtMjUwIGVwb2NfZGF0YSIgdXNpbmcgOCAgd2l0aCBzdGVwcyB0aXRsZSAiUDciCnBsb3Qg
        IjwgdGFpbCAtMjUwIGVwb2NfZGF0YSIgdXNpbmcgOSAgd2l0aCBzdGVwcyB0aXRsZSAiTzEi
        CnBsb3QgIjwgdGFpbCAtMjUwIGVwb2NfZGF0YSIgdXNpbmcgMTAgd2l0aCBzdGVwcyB0aXRs
        ZSAiTzIiCnBsb3QgIjwgdGFpbCAtMjUwIGVwb2NfZGF0YSIgdXNpbmcgMTEgd2l0aCBzdGVw
        cyB0aXRsZSAiUDgiCnBsb3QgIjwgdGFpbCAtMjUwIGVwb2NfZGF0YSIgdXNpbmcgMTIgd2l0
        aCBzdGVwcyB0aXRsZSAiVDgiCnBsb3QgIjwgdGFpbCAtMjUwIGVwb2NfZGF0YSIgdXNpbmcg
        MTMgd2l0aCBzdGVwcyB0aXRsZSAiRjgiCnBsb3QgIjwgdGFpbCAtMjUwIGVwb2NfZGF0YSIg
        dXNpbmcgMTQgd2l0aCBzdGVwcyB0aXRsZSAiQUY0IgpwbG90ICI8IHRhaWwgLTI1MCBlcG9j
        X2RhdGEiIHVzaW5nIDE1IHdpdGggc3RlcHMgdGl0bGUgIkZDNiIKcGxvdCAiPCB0YWlsIC0y
        NTAgZXBvY19kYXRhIiB1c2luZyAxNiB3aXRoIHN0ZXBzIHRpdGxlICJGNCIKdW5zZXQgbXVs
        dGlwbG90CnJlcmVhZApyZXBsb3QK
        """
        tf = tempfile.NamedTemporaryFile(delete=False)
        psname = tf.name
        tf.write(plot_script.decode("base64"))
        tf.close()
        
        args.tempfiles.append(tf.name)

        procs = []

        procs.append(subprocess.Popen(["python",rsname]))
        procs.append(subprocess.Popen(["gnuplot","-p",psname]))

        for proc in procs:
                proc.wait()
else:
        raise NotImplementedError("sensor not specified")
