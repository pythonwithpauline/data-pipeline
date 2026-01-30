from __future__ import annotations


def clean_record(rec: dict, *, lowercase_email: bool, strip_whitespace: bool) -> dict:
    out = dict(rec)

    if strip_whitespace:
        for k, v in list(out.items()):
            if isinstance(v, str):
                out[k] = v.strip()

    if lowercase_email and isinstance(out.get("email"), str):
        out["email"] = out["email"].lower()

    return out
