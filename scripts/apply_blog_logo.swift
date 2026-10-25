import AppKit
import Foundation

guard CommandLine.arguments.count == 4 else {
    fputs("usage: apply_blog_logo.swift <cover.png> <logo.png> <output.png>\n", stderr)
    exit(2)
}

let coverURL = URL(fileURLWithPath: CommandLine.arguments[1])
let logoURL = URL(fileURLWithPath: CommandLine.arguments[2])
let outputURL = URL(fileURLWithPath: CommandLine.arguments[3])

guard
    let cover = NSImage(contentsOf: coverURL),
    let logo = NSImage(contentsOf: logoURL),
    let coverCG = cover.cgImage(forProposedRect: nil, context: nil, hints: nil),
    let logoCG = logo.cgImage(forProposedRect: nil, context: nil, hints: nil)
else {
    fputs("could not load input images\n", stderr)
    exit(1)
}

let width = coverCG.width
let height = coverCG.height
guard let bitmap = NSBitmapImageRep(
    bitmapDataPlanes: nil,
    pixelsWide: width,
    pixelsHigh: height,
    bitsPerSample: 8,
    samplesPerPixel: 4,
    hasAlpha: true,
    isPlanar: false,
    colorSpaceName: .deviceRGB,
    bytesPerRow: 0,
    bitsPerPixel: 0
) else {
    fputs("could not create output bitmap\n", stderr)
    exit(1)
}

NSGraphicsContext.saveGraphicsState()
guard let context = NSGraphicsContext(bitmapImageRep: bitmap) else {
    fputs("could not create graphics context\n", stderr)
    exit(1)
}
NSGraphicsContext.current = context
context.imageInterpolation = .high

NSImage(cgImage: coverCG, size: NSSize(width: width, height: height)).draw(
    in: NSRect(x: 0, y: 0, width: width, height: height)
)

// Remove the generated lockup only. Coordinates use AppKit's bottom-left origin.
NSColor.white.setFill()
NSBezierPath(rect: NSRect(x: 35, y: height - 190, width: 485, height: 175)).fill()

// Source crops are taken from the official square logo artwork.
let markCrop = CGRect(x: 120, y: 130, width: 1030, height: 760)
let nameCrop = CGRect(x: 145, y: 870, width: 970, height: 255)

guard
    let markCG = logoCG.cropping(to: markCrop),
    let nameCG = logoCG.cropping(to: nameCrop)
else {
    fputs("could not crop official logo\n", stderr)
    exit(1)
}

let mark = NSImage(cgImage: markCG, size: NSSize(width: markCG.width, height: markCG.height))
let name = NSImage(cgImage: nameCG, size: NSSize(width: nameCG.width, height: nameCG.height))

mark.draw(in: NSRect(x: 48, y: height - 174, width: 160, height: 128))
name.draw(in: NSRect(x: 203, y: height - 158, width: 300, height: 82))

context.flushGraphics()
NSGraphicsContext.restoreGraphicsState()

guard let png = bitmap.representation(using: .png, properties: [:]) else {
    fputs("could not encode png\n", stderr)
    exit(1)
}

try png.write(to: outputURL)
